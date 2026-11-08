/* ═══════════════════════════════════════════════════════════════
   FOOTBALL INTEL — hit rates
   "How many of his games has this player reached X?"  Computed in the
   browser from players/latest.json game logs, so there is nothing to
   rebuild: whenever the data refresh updates the logs, every hit rate
   updates with it. Shared by players.html, threats.html, hit_rates.html.
   ═══════════════════════════════════════════════════════════════ */

/* Benchmark ladders. Keys are the stat names used in each game's `m`. */
const HR_LADDER = {
  QB: { pass_yds: [200, 225, 250, 275, 300], pass_td: [1, 2, 3] },
  RB: { rush_yds: [30, 40, 50, 60, 70, 80, 100], rec_yds: [15, 20, 30, 40, 50], rec: [2, 3, 4, 5] },
  WR: { rec_yds: [30, 40, 50, 60, 70, 80, 100], rec: [3, 4, 5, 6, 7] },
  TE: { rec_yds: [30, 40, 50, 60, 70, 80, 100], rec: [3, 4, 5, 6] },
};
const HR_LABEL = { pass_yds: 'Passing yds', pass_td: 'Passing TDs', rush_yds: 'Rushing yds',
                   rec_yds: 'Receiving yds', rec: 'Receptions' };
const HR_UNIT  = { pass_yds: 'yds', pass_td: 'TD', rush_yds: 'yds', rec_yds: 'yds', rec: 'rec' };
/* Threats page category -> hit-rate stat */
const HR_FROM_THREAT = { pass_yds: 'pass_yds', pass_tds: 'pass_td', rush_yds: 'rush_yds', rec_yds: 'rec_yds', rec: 'rec' };

const HR_MIN_GAMES = 4;      // fewer games than this is too thin to call a "rate"
const HR_THRESHOLD = 0.75;   // a benchmark counts as reliable at 75%+

const hrNorm = s => String(s || '').toLowerCase().replace(/[.'’]/g, '')
  .replace(/\b(jr|sr|ii|iii|iv|v)\b/g, '').replace(/[^a-z]/g, '');

/* Ladder for one player through a given week (inclusive). thruWeek omitted = whole season. */
function hrCompute(player, thruWeek){
  const ladders = HR_LADDER[player.pos || player._pos] || {};
  const log = (player.log || []).filter(g => thruWeek == null || g.week <= thruWeek);
  const out = {};
  for (const [stat, rungs] of Object.entries(ladders)){
    const vals = log.map(g => g.m && g.m[stat]).filter(v => v != null);
    out[stat] = { games: vals.length,
      rungs: rungs.map(t => { const hits = vals.filter(v => v >= t).length;
                              return { t, hits, pct: vals.length ? hits / vals.length : 0 }; }) };
  }
  return out;
}
/* Highest rung with pct >= minPct (default 75%). null if none or too few games. */
function hrBest(statResult, minPct, minGames){
  if (!statResult || statResult.games < (minGames == null ? HR_MIN_GAMES : minGames)) return null;
  const need = minPct == null ? HR_THRESHOLD : minPct;
  let best = null;
  for (const r of statResult.rungs) if (r.pct >= need - 1e-9) best = r;
  return best;
}
/* The rung with the highest hit count at or above 50%, for "no 75% benchmark" messages. */
function hrNearest(statResult){
  if (!statResult || !statResult.games) return null;
  let best = null;
  for (const r of statResult.rungs) if (r.pct >= 0.5) best = r;
  return best;
}
function hrText(stat, rung, games){
  const t = rung.t;
  const what = stat === 'pass_td' || stat === 'rec' ? `${t}+ ${HR_UNIT[stat]}` : `${t}+ yds`;
  return `${what} in ${rung.hits}/${games} games`;
}
function hrPctClass(p){ return p >= 0.9 ? 'hr-a' : p >= 0.75 ? 'hr-b' : p >= 0.5 ? 'hr-c' : 'hr-d'; }

/* Index of every 2026 player so threats/starters can be looked up by name + position. */
function hrIndex(playersData){
  const idx = {};
  for (const [pos, rows] of Object.entries(playersData.players || {}))
    for (const p of rows){ p._pos = pos; idx[hrNorm(p.name) + '|' + pos] = p; }
  return idx;
}
function hrLookup(idx, name, pos){ return idx[hrNorm(name) + '|' + pos] || null; }

/* Full ladder card for one player (used on the Players page). */
function hrLadderHTML(player, thruWeek){
  const res = hrCompute(player, thruWeek), pos = player.pos || player._pos;
  const blocks = Object.keys(HR_LADDER[pos] || {}).map(stat => {
    const r = res[stat], best = hrBest(r);
    const head = best ? `<span class="hr-chip ${hrPctClass(best.pct)}">${hrText(stat, best, r.games)} \u00b7 <b>${Math.round(100 * best.pct)}%</b></span>`
      : `<span class="hr-none">${r.games < HR_MIN_GAMES ? 'Only ' + r.games + ' game' + (r.games === 1 ? '' : 's') + ' so far' : 'No benchmark reached in 75%+ of games'}</span>`;
    const rows = r.rungs.map(g => `<div class="hr-rung${best && g.t === best.t ? ' best' : ''}">
        <span class="hr-t">${g.t}+${stat === 'rec' || stat === 'pass_td' ? '' : ' yds'}</span>
        <span class="hr-bar"><i class="${hrPctClass(g.pct)}" style="width:${Math.round(100 * g.pct)}%"></i></span>
        <span class="hr-n">${g.hits}/${r.games}</span><span class="hr-p">${Math.round(100 * g.pct)}%</span></div>`).join('');
    return `<div class="hr-block"><div class="hr-head"><b>${HR_LABEL[stat]}</b>${head}</div>${rows}</div>`;
  }).join('');
  return `<div class="hr-wrap">${blocks}<div class="hr-foot">Counts games this season in which he reached each mark. Highlighted = highest mark reached in 75%+ of games (needs ${HR_MIN_GAMES}+ games).</div></div>`;
}

const HR_CSS = `
.hr-wrap{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin-top:6px}
.hr-block{border:1px solid var(--border);border-radius:var(--radius);padding:11px 12px;background:var(--surface)}
.hr-head{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px;font-size:12.5px}
.hr-rung{display:grid;grid-template-columns:62px 1fr 42px 40px;gap:8px;align-items:center;padding:3px 4px;border-radius:4px;
  font-family:var(--font-mono);font-size:11px;color:var(--text-mid)}
.hr-rung.best{background:rgba(74,222,128,.08);color:var(--text)}
.hr-bar{height:6px;border-radius:3px;background:var(--surface2);overflow:hidden}
.hr-bar i{display:block;height:100%;border-radius:3px;background:currentColor}
.hr-bar i.hr-a{color:#4ade80}.hr-bar i.hr-b{color:#86efac}.hr-bar i.hr-c{color:#facc15}.hr-bar i.hr-d{color:#64748b}
.hr-n,.hr-p{text-align:right;font-variant-numeric:tabular-nums}
.hr-foot{grid-column:1/-1;font-family:var(--font-mono);font-size:10px;color:var(--text-dim);line-height:1.6}
`;
const HR_CSS_BASE = `
.hr-chip{display:inline-flex;align-items:center;gap:6px;font-family:var(--font-mono);font-size:10.5px;
  padding:2px 8px;border-radius:5px;border:1px solid var(--border);white-space:nowrap}
.hr-chip b{font-weight:700}
.hr-a{color:#4ade80;border-color:rgba(74,222,128,.5);background:rgba(74,222,128,.09)}
.hr-b{color:#86efac;border-color:rgba(134,239,172,.4);background:rgba(134,239,172,.07)}
.hr-c{color:#facc15;border-color:rgba(250,204,21,.4);background:rgba(250,204,21,.07)}
.hr-d{color:var(--text-mid)}
.hr-none{font-family:var(--font-mono);font-size:10px;color:var(--text-dim)}
`;
if (typeof document !== 'undefined'){
  const st = document.createElement('style'); st.textContent = HR_CSS_BASE + HR_CSS; document.head.appendChild(st);
}
