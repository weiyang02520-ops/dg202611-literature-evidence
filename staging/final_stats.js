const fs = require('fs');
const t = fs.readFileSync(__dirname + '/../01_RAW_LITERATURE_POOL.csv', 'utf8').replace(/^\uFEFF/, '');
const rows = []; let row = [], f = '', q = false;
for (let i = 0; i < t.length; i++) {
  const c = t[i];
  if (q) { if (c === '"') { if (t[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += c; }
  else if (c === '"') q = true;
  else if (c === ',') { row.push(f); f = ''; }
  else if (c === '\n') { row.push(f); rows.push(row); row = []; f = ''; }
  else if (c !== '\r') f += c;
}
if (f.length || row.length) { row.push(f); rows.push(row); }
const h = rows[0];
const iA = h.indexOf('Research Area'), iR = h.indexOf('Real/Simulation/Dataset'), iY = h.indexOf('Year'), iS = h.indexOf('Verification Status'), iP = h.indexOf('Perf_Data_Count');
const rs = {}, decade = {}, st = {};
let withPerf = 0;
for (let r = 1; r < rows.length; r++) {
  const a = rows[r][iR]; rs[a] = (rs[a] || 0) + 1;
  const s = rows[r][iS]; st[s] = (st[s] || 0) + 1;
  const y = parseInt(rows[r][iY]);
  if (y >= 2020) decade['2020-2026'] = (decade['2020-2026'] || 0) + 1;
  else if (y >= 2015) decade['2015-2019'] = (decade['2015-2019'] || 0) + 1;
  else decade['2014及以前'] = (decade['2014及以前'] || 0) + 1;
  if (parseInt(rows[r][iP]) > 0) withPerf++;
}
console.log('总条目:', rows.length - 1);
console.log('验证状态:', JSON.stringify(st));
console.log('类型分布:', JSON.stringify(rs));
console.log('年代分布:', JSON.stringify(decade));
console.log('含性能数据条目:', withPerf);
const bib = fs.readFileSync(__dirname + '/../references.bib', 'utf8');
console.log('bib条目:', (bib.match(/^@/gm) || []).length);
