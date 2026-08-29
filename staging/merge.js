// 合并 8 个研究组的 raw JSON -> 01_RAW_LITERATURE_POOL.csv + 03 矩阵初稿 + digest
const fs = require('fs');
const path = require('path');
const DIR = __dirname + '/..';
const STG = __dirname;

const groups = ['UWB', 'RADAR', 'EVENT', 'FUSION', 'GNSS', 'LIDAR', 'RELOCSYNC', 'SIM'];
const AREA_LABEL = { UWB: 'UWB', RADAR: 'mmWave Radar', EVENT: 'Event Camera', FUSION: 'Adaptive Fusion', GNSS: 'GNSS/BeiDou/RTK', LIDAR: 'LiDAR Degeneracy/Dynamic', RELOCSYNC: 'Relocalization/Sync-Calib', SIM: 'Simulation' };
const SUB_LABEL = { GNSS: 'GNSS', BDS_SMS: 'BeiDou SMS', FUTURE_OUTLOOK: 'Future Outlook', DEGENERACY: 'LiDAR Degeneracy', DYNAMIC: 'LiDAR Dynamic', RELOC: 'Relocalization', SYNC: 'Sync/Calibration', SIM: 'Simulation' };

function normTitle(t) {
  return String(t || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim().replace(/\s+/g, ' ');
}
function normDoi(d) {
  return String(d || '').toLowerCase().replace(/^https?:\/\/(dx\.)?doi\.org\//, '').replace(/[^a-z0-9./-]/g, '');
}
function escCsv(v) {
  const s = String(v == null ? '' : v).replace(/\r?\n/g, ' ').replace(/"/g, '""');
  return /[",;]/.test(s) ? '"' + s + '"' : s;
}
function authStr(a) { return Array.isArray(a) ? a.join('; ') : String(a || ''); }

const papers = [];
const dupLog = [];
const idCounters = {};

for (const g of groups) {
  const raw = JSON.parse(fs.readFileSync(path.join(STG, g + '_raw.json'), 'utf8'));
  for (const p of (raw.papers || [])) {
    const sub = p.subarea || null;
    const areaLabel = SUB_LABEL[sub] || AREA_LABEL[g] || g;
    const prefix = ({ GNSS: 'GNSS', BDS_SMS: 'BDS', FUTURE_OUTLOOK: 'FUT', DEGENERACY: 'LDG', DYNAMIC: 'LDY', RELOC: 'RLC', SYNC: 'SYN', SIM: 'SIM' })[sub] || g;
    idCounters[prefix] = (idCounters[prefix] || 0) + 1;
    const id = prefix + '-' + String(idCounters[prefix]).padStart(2, '0');
    papers.push({
      id, group: g, areaLabel,
      title: String(p.title || '').trim(),
      authors: authStr(p.authors), year: p.year || null, venue: p.venue || null,
      doi: p.doi || null, arxiv_id: p.arxiv_id || null, url: p.url || null,
      keywords: Array.isArray(p.keywords) ? p.keywords.join('; ') : (p.keywords || ''),
      real_or_sim: p.real_or_sim || 'UNKNOWN',
      relevance: p.potential_relevance || '',
      status: p.verification_status || 'UNVERIFIED',
      evidence: p.verification_evidence || '',
      perf: Array.isArray(p.performance_data) ? p.performance_data.filter(x => x && (x.value != null && x.value !== '')) : [],
      core: !!p.candidate_core,
      notes: p.notes || '',
    });
  }
}

// 去重（标题归一 + DOI + arXiv）
const seen = new Map();
const finalList = [];
for (const p of papers) {
  const keys = [];
  if (p.doi) keys.push('doi:' + normDoi(p.doi));
  if (p.arxiv_id) keys.push('ax:' + String(p.arxiv_id).replace(/v\d+$/, '').trim());
  const nt = normTitle(p.title);
  if (nt.length > 15) keys.push('t:' + nt);
  let dupOf = null;
  for (const k of keys) { if (seen.has(k)) { dupOf = seen.get(k); break; } }
  if (dupOf && normTitle(p.title) === normTitle(dupOf.title)) {
    // 合并进主条目
    dupOf.areaLabel += ' + ' + p.areaLabel;
    dupOf.core = dupOf.core || p.core;
    dupOf.dupGroups = (dupOf.dupGroups || []) + ',' + p.group;
    dupLog.push({ kept: dupOf.id, dropped: p.id, title: p.title, groups: dupOf.group + '+' + p.group });
    for (const pf of p.perf) {
      if (!dupOf.perf.some(q => (q.metric || '') === (pf.metric || '') && String(q.value) === String(pf.value))) dupOf.perf.push(pf);
    }
    if (p.status === 'VERIFIED' && dupOf.status !== 'VERIFIED') dupOf.status = 'VERIFIED';
    continue;
  }
  for (const k of keys) seen.set(k, p);
  finalList.push(p);
}

// ---------- 01_RAW_LITERATURE_POOL.csv ----------
const poolCols = ['ID', 'Title', 'Authors', 'Year', 'Venue', 'DOI', 'arXiv_ID', 'URL', 'Research Area', 'Keywords', 'Real/Simulation/Dataset', 'Potential Relevance', 'Verification Status', 'Verification Evidence', 'Perf_Data_Count', 'Candidate_Core', 'Notes'];
let csv = '\uFEFF' + poolCols.join(',') + '\n';
for (const p of finalList) {
  csv += [p.id, p.title, p.authors, p.year, p.venue, p.doi, p.arxiv_id, p.url, p.areaLabel, p.keywords, p.real_or_sim, p.relevance, p.status, p.evidence, p.perf.length, p.core ? 'YES' : 'NO', p.notes + (p.dupGroups ? ' [cross-area merge:' + p.dupGroups + ']' : '')].map(escCsv).join(',') + '\n';
}
fs.writeFileSync(DIR + '/01_RAW_LITERATURE_POOL.csv', csv);

// ---------- 03_PERFORMANCE_BENCHMARK_MATRIX.csv 初稿 ----------
const mCols = ['Matrix_ID', 'Paper_ID', 'Technology', 'Year', 'Scenario', 'Real_Sim_Dataset', 'Sensors', 'Hardware', 'Ground_Truth', 'Metric', 'Metric_Definition', 'Value', 'Unit', 'LOS_NLOS', 'Degradation', 'Test_Distance', 'Test_Duration', 'Source_Level', 'Snippet', 'Limitations', 'Safe_Project_Claim', 'Can_Compare_To_Our_Project', 'Reason', 'EXTRACTION_VERIFIED'];
let m = '\uFEFF' + mCols.join(',') + '\n';
let mi = 0;
const perfRows = [];
for (const p of finalList) {
  for (const pf of p.perf) {
    mi++;
    const row = {
      Matrix_ID: 'PM-' + String(mi).padStart(3, '0'), Paper_ID: p.id, Technology: p.areaLabel, Year: p.year,
      Scenario: pf.conditions || '', Real_Sim_Dataset: p.real_or_sim, Sensors: '', Hardware: '', Ground_Truth: '',
      Metric: pf.metric || '', Metric_Definition: '', Value: String(pf.value ?? ''), Unit: pf.unit || '',
      LOS_NLOS: /NLOS/i.test((pf.conditions || '') + ' ' + (pf.metric || '') + ' ' + (pf.snippet || '')) ? (/LOS/i.test(pf.conditions || '') ? 'LOS+NLOS' : 'NLOS-related') : (/LOS/i.test(pf.conditions || '') ? 'LOS' : 'UNSPECIFIED'),
      Degradation: /denied|outage|degrad|遮挡|拒止|雾|雨|烟|暗光|强光|NLOS/i.test((pf.conditions || '') + ' ' + (pf.snippet || '')) ? 'DEGRADED-RELATED' : 'UNSPECIFIED',
      Test_Distance: '', Test_Duration: '', Source_Level: pf.source_level || 'UNCERTAIN', Snippet: pf.snippet || '',
      Limitations: '', Safe_Project_Claim: '', Can_Compare_To_Our_Project: '', Reason: '', EXTRACTION_VERIFIED: 'PENDING',
      _paperTitle: p.title,
    };
    perfRows.push(row);
    m += [row.Matrix_ID, row.Paper_ID, row.Technology, row.Year, row.Scenario, row.Real_Sim_Dataset, row.Sensors, row.Hardware, row.Ground_Truth, row.Metric, row.Metric_Definition, row.Value, row.Unit, row.LOS_NLOS, row.Degradation, row.Test_Distance, row.Test_Duration, row.Source_Level, row.Snippet, row.Limitations, row.Safe_Project_Claim, row.Can_Compare_To_Our_Project, row.Reason, row.EXTRACTION_VERIFIED].map(escCsv).join(',') + '\n';
  }
}
fs.writeFileSync(DIR + '/03_PERFORMANCE_BENCHMARK_MATRIX.csv', m);

// ---------- 03b 核验任务清单（给 Wave2 验证代理） ----------
const verifyTask = perfRows.map(r => ({ Matrix_ID: r.Matrix_ID, Paper_ID: r.Paper_ID, title: r._paperTitle, arxiv_id: (finalList.find(p => p.id === r.Paper_ID) || {}).arxiv_id, doi: (finalList.find(p => p.id === r.Paper_ID) || {}).doi, metric: r.Metric, value: r.Value, unit: r.Unit, conditions: r.Scenario, source_level: r.Source_Level, snippet: r.Snippet }));
fs.writeFileSync(STG + '/verify_task.json', JSON.stringify(verifyTask, null, 1));

// ---------- digests ----------
const digestCore = finalList.filter(p => p.core).map(p => ({ id: p.id, title: p.title, year: p.year, venue: p.venue, area: p.areaLabel, status: p.status, nperf: p.perf.length, metrics: p.perf.map(x => x.metric + '=' + x.value + ' ' + (x.unit || '')).slice(0, 6), relevance: p.relevance }));
fs.writeFileSync(STG + '/digest_core.json', JSON.stringify(digestCore, null, 1));
const digestAll = finalList.map(p => ({ id: p.id, t: p.title.slice(0, 90), y: p.year, v: p.venue, a: p.areaLabel, s: p.status, n: p.perf.length, c: p.core ? 1 : 0 }));
fs.writeFileSync(STG + '/digest_all.json', JSON.stringify(digestAll, null, 1));

// ---------- search logs 合并 ----------
let slOut = { merged: [] };
for (const g of groups.concat(['DATASETS', 'OPENSOURCE'])) {
  const f = path.join(STG, g + '_searchlog.json');
  if (fs.existsSync(f)) {
    try { const d = JSON.parse(fs.readFileSync(f, 'utf8')); slOut.merged.push({ area: d.area || g, queries: d.queries || [] }); } catch (e) { slOut.merged.push({ area: g, error: String(e) }); }
  }
}
fs.writeFileSync(STG + '/searchlog_merged.json', JSON.stringify(slOut, null, 1));

// ---------- rejected 合并 ----------
const rej = [];
const rejSrc = { UWB: 'UWB', RADAR: 'RADAR', EVENT: 'EVENT', FUSION: 'FUSION', GNSS: 'GNSS', LIDAR: 'LIDAR', RELOCSYNC: 'RELOCSYNC', SIM: 'SIM', DATASETS: 'DATASETS', OPENSOURCE: 'OPENSOURCE' };
let ri = 0;
for (const g of Object.keys(rejSrc)) {
  const f = path.join(STG, g + '_raw.json');
  if (!fs.existsSync(f)) continue;
  try {
    const d = JSON.parse(fs.readFileSync(f, 'utf8'));
    for (const r of (d.rejected || [])) { ri++; rej.push({ id: 'RJ-' + String(ri).padStart(3, '0'), group: g, ...r }); }
  } catch (e) { }
}
fs.writeFileSync(STG + '/rejected_merged.json', JSON.stringify(rej, null, 1));

// ---------- conflicts 合并 ----------
const con = []; let ci = 0;
for (const g of groups.concat(['DATASETS', 'OPENSOURCE'])) {
  const f = path.join(STG, g + '_raw.json');
  if (!fs.existsSync(f)) continue;
  try {
    const d = JSON.parse(fs.readFileSync(f, 'utf8'));
    for (const c of (d.conflicts || [])) { ci++; con.push({ id: 'CF-' + String(ci).padStart(2, '0'), group: g, ...c }); }
  } catch (e) { }
}
fs.writeFileSync(STG + '/conflicts_merged.json', JSON.stringify(con, null, 1));

// ---------- references.bib（全部 VERIFIED + PARTIALLY_VERIFIED） ----------
function bibKey(p) {
  const ln = (p.authors.split(';')[0] || 'anon').trim().split(/\s+/).pop().replace(/[^A-Za-z]/g, '') || 'anon';
  const w = normTitle(p.title).split(' ').slice(0, 3).map(s => s && s[0].toUpperCase() + s.slice(1)).join('');
  return ln + (p.year || 'n.d.') + (w || 'Item');
}
function bibField(s) { return String(s == null ? '' : s).replace(/[{}]/g, '').replace(/\s+/g, ' ').trim(); }
const used = new Map();
let bib = '% DG-202611 literature research - references for all VERIFIED / PARTIALLY_VERIFIED pool entries\n% Auto-generated ' + new Date().toISOString().slice(0, 10) + ' from 01_RAW_LITERATURE_POOL.csv\n\n';
for (const p of finalList) {
  if (p.status === 'REJECTED' || p.status === 'UNVERIFIED') continue;
  let k = bibKey(p); if (used.has(k)) { let i = 2; while (used.has(k + i)) i++; k = k + i; } used.set(k, 1);
  const a = p.authors.split(';').map(s => s.trim()).filter(Boolean).map(s => { const parts = s.split(/\s+/); return parts.length > 1 ? parts.slice(0, -1).join(' ') + ', ' + parts.slice(-1)[0] : s; }).join(' and ');
  let e = '@misc{' + k + ',\n';
  e += '  title = {' + bibField(p.title) + '},\n';
  if (a) e += '  author = {' + bibField(a) + '},\n';
  if (p.year) e += '  year = {' + p.year + '},\n';
  if (p.venue) e += '  howpublished = {' + bibField(p.venue) + '},\n';
  if (p.doi) e += '  doi = {' + bibField(p.doi) + '},\n';
  if (p.arxiv_id) e += '  eprint = {' + bibField(p.arxiv_id) + '},\n  archivePrefix = {arXiv},\n';
  if (p.url) e += '  url = {' + bibField(p.url) + '},\n';
  e += '  note = {' + p.id + '; ' + p.status + (p.status !== 'VERIFIED' ? ' - verify before formal citation' : '') + '}\n}\n\n';
  bib += e;
}
fs.writeFileSync(DIR + '/references.bib', bib);

// ---------- 统计 ----------
const stats = {
  total_before_dedup: papers.length, total_after_dedup: finalList.length, duplicates_merged: dupLog.length,
  by_status: {}, by_area: {}, papers_with_perf: finalList.filter(p => p.perf.length > 0).length, perf_rows: perfRows.length,
  core_candidates: finalList.filter(p => p.core).length,
  perf_by_source_level: perfRows.reduce((a, r) => { a[r.Source_Level] = (a[r.Source_Level] || 0) + 1; return a; }, {}),
  rejected_entries: rej.length, conflict_entries: con.length, bib_entries: used.size,
};
for (const p of finalList) { stats.by_status[p.status] = (stats.by_status[p.status] || 0) + 1; stats.by_area[p.areaLabel] = (stats.by_area[p.areaLabel] || 0) + 1; }
fs.writeFileSync(STG + '/merge_stats.json', JSON.stringify({ stats, duplicates: dupLog }, null, 1));
console.log(JSON.stringify(stats, null, 2));
console.log('DUP LIST:', JSON.stringify(dupLog.map(d => d.kept + '<-' + d.dropped + ' [' + d.title.slice(0, 40) + ']'), null, 1));
