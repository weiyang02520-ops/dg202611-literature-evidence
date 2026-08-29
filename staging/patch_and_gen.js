// 把 V1/V2 核验结果写回 03 矩阵；生成 10_REJECTED_OR_UNVERIFIED.md 与 11_SEARCH_LOG.md
const fs = require('fs');
const DIR = __dirname + '/..';

// --- 简易 CSV 解析（处理引号） ---
function parseCsv(text) {
  text = text.replace(/^\uFEFF/, '');
  const rows = []; let row = [], field = '', inQ = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (inQ) {
      if (c === '"') { if (text[i + 1] === '"') { field += '"'; i++; } else inQ = false; }
      else field += c;
    } else if (c === '"') inQ = true;
    else if (c === ',') { row.push(field); field = ''; }
    else if (c === '\n') { row.push(field); rows.push(row); row = []; field = ''; }
    else if (c !== '\r') field += c;
  }
  if (field.length || row.length) { row.push(field); rows.push(row); }
  return rows;
}

// --- 1) patch 03 ---
const csvRaw = fs.readFileSync(DIR + '/03_PERFORMANCE_BENCHMARK_MATRIX.csv', 'utf8');
const rows = parseCsv(csvRaw);
const header = rows[0];
const iMV = header.indexOf('EXTRACTION_VERIFIED');
const iReason = header.indexOf('Reason');
const iSafe = header.indexOf('Safe_Project_Claim');
const iMid = header.indexOf('Matrix_ID');
const verdicts = {};
for (const f of ['staging/VERIFY_report_V1.json', 'staging/VERIFY_report_V2.json']) {
  for (const v of JSON.parse(fs.readFileSync(DIR + '/' + f, 'utf8'))) verdicts[v.Matrix_ID] = v;
}
const flags = [];
let patched = 0;
for (let r = 1; r < rows.length; r++) {
  const mid = rows[r][iMid];
  const v = verdicts[mid];
  if (v) {
    rows[r][iMV] = v.verdict;
    if (v.verdict === 'NO') {
      rows[r][iSafe] = 'NO';
      rows[r][iReason] = '独立核验未在原文找到该数字: ' + (v.note || '');
    } else if (v.verdict === 'PARTIAL') {
      rows[r][iReason] = '核验有歧义: ' + (v.note || '');
    } else if (v.verdict === 'YES') {
      rows[r][iReason] = '独立核验通过: ' + (v.checked_url || '');
    }
    patched++;
  } else {
    rows[r][iMV] = 'NOT_VERIFIED';
    rows[r][iReason] = '抽样核验未覆盖本行；引用前需按 Source_Level 自行回查原文';
  }
  flags.push({ Matrix_ID: mid, Paper_ID: rows[r][header.indexOf('Paper_ID')], Metric: rows[r][header.indexOf('Metric')], Value: rows[r][header.indexOf('Value')], EV: rows[r][iMV] });
}
// 重新转义输出
function esc(v) { const s = String(v == null ? '' : v).replace(/\r?\n/g, ' ').replace(/"/g, '""'); return /[",;]/.test(s) ? '"' + s + '"' : s; }
let out = '\uFEFF' + header.join(',') + '\n';
for (let r = 1; r < rows.length; r++) out += rows[r].map(esc).join(',') + '\n';
fs.writeFileSync(DIR + '/03_PERFORMANCE_BENCHMARK_MATRIX.csv', out);
fs.writeFileSync(__dirname + '/perf_flags.json', JSON.stringify(flags, null, 1));
console.log('03 patched rows:', patched, '/', rows.length - 1);

// --- 2) 10_REJECTED_OR_UNVERIFIED.md ---
const rej = JSON.parse(fs.readFileSync(__dirname + '/rejected_merged.json', 'utf8'));
const byGroup = {};
for (const r of rej) (byGroup[r.group] = byGroup[r.group] || []).push(r);
let m10 = `# 10 REJECTED OR UNVERIFIED — 淘汰与未核验记录

生成日期：2026-08-29
本文件记录文献挖掘过程中被拒绝或未能核验的候选条目。**任何条目均未混入正式文献库**；记录在此以保证过程可复查、不静默丢弃。
另含第二层性能核验发现的 5 处问题（文件末尾「性能数字核验发现的问题」节）。

总计：${rej.length} 条 rejected 记录。

`;
for (const g of Object.keys(byGroup)) {
  m10 += `\n## ${g} 组（${byGroup[g].length} 条）\n\n| # | Claimed | Final Status | Reason | Verification Attempt |\n|---|---|---|---|---|\n`;
  byGroup[g].forEach((r, i) => {
    const claimed = String(r.claimed || r.claim || r.name || r.title || JSON.stringify(r)).slice(0, 120).replace(/\|/g, '/');
    const status = r.final_status || r.status || 'REJECTED';
    const reason = String(r.reason || r.reason_rejected || '').slice(0, 200).replace(/\|/g, '/');
    const attempt = String(r.verification_attempt || r.attempt || '').slice(0, 200).replace(/\|/g, '/');
    m10 += `| ${g}-${i + 1} | ${claimed} | ${status} | ${reason} | ${attempt} |\n`;
  });
}
// 附加性能核验问题
const flags2 = JSON.parse(fs.readFileSync(__dirname + '/perf_flags.json', 'utf8'));
const noRows = flags2.filter(f => f.EV === 'NO');
m10 += `\n## 性能数字核验发现的问题（Wave2 独立核验）\n\n以下行在第二层核验中未能在原文找到对应数字，已在该行的 Reason 列标注，**禁止引用**：\n\n`;
for (const r of noRows) m10 += `- ${r.Matrix_ID}（${r.Paper_ID}）：${r.Metric} = ${r.Value} —— 核验代理在原文未找到该数字\n`;
m10 += `\n注：除 NO 行外，另有 PARTIAL 行（口径歧义）与 NOT_VERIFIED 行（抽样未覆盖），详见 03 矩阵 EXTRACTION_VERIFIED 列。\n`;
fs.writeFileSync(DIR + '/10_REJECTED_OR_UNVERIFIED.md', m10);
console.log('10 written, rejected:', rej.length, 'no-rows:', noRows.length);

// --- 3) 11_SEARCH_LOG.md ---
const sl = JSON.parse(fs.readFileSync(__dirname + '/searchlog_merged.json', 'utf8'));
let m11 = `# 11 SEARCH LOG — 检索日志

生成日期：2026-08-29
本文件汇总 8 个研究组全部检索查询（含失败与限流记录），供复查检索覆盖面与复现。

总查询记录：${sl.merged.reduce((a, g) => a + (g.queries || []).length, 0)} 条（覆盖 ${sl.merged.length} 个组；个别组另执行了批量 DOI 解析等未逐条计数的操作，详见各组日志原文 staging/*_searchlog.json）。

`;
let qi = 0;
for (const g of sl.merged) {
  m11 += `\n## ${g.area} 组（${(g.queries || []).length} 条）\n\n| # | Query | Tool | Screened | Accepted | Rejected | Notes |\n|---|---|---|---|---|---|---|\n`;
  for (const q of (g.queries || [])) {
    qi++;
    const e = s => String(s == null ? '' : s).replace(/\|/g, '/').slice(0, 150);
    m11 += `| ${qi} | ${e(q.query)} | ${e(q.tool)} | ${e(q.screened)} | ${e(q.accepted)} | ${e(q.rejected)} | ${e(q.notes)} |\n`;
  }
}
fs.writeFileSync(DIR + '/11_SEARCH_LOG.md', m11);
console.log('11 written, queries:', qi);
