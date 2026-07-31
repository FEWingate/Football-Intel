/* ═══════════════════════════════════════════════════════════════
   FOOTBALL INTEL — shared shell
   Renders header, sidebar nav, mobile nav and theme handling so
   every page inherits the same chrome. Add a page by appending to
   NAV below and setting <body data-page="key">.
   ═══════════════════════════════════════════════════════════════ */

const NAV = [
  { key: 'threats',  label: 'Threats',      ico: '⚡', href: 'threats.html' },
  { key: 'matchup',  label: 'Matchup Stats',ico: '⚔️', href: 'matchup_stats.html' },
  { key: 'context',  label: 'Contextual',   ico: '📊', href: 'contextual_stats.html' },
  { key: 'games',    label: 'Games',        ico: '📅', href: 'games.html' },
  { key: 'teams',    label: 'Teams',        ico: '🛡️' },
  { key: 'players',  label: 'Players',      ico: '👤' },
  { key: 'dfs',      label: 'DFS Center',   ico: '💰' },
  { key: 'props',    label: 'Prop Center',  ico: '🎯' },
  { key: 'injuries', label: 'Injuries',     ico: '🩹' },
  { key: 'standings',label: 'Standings',    ico: '🏆' },
  { key: 'stats',    label: 'Stats Hub',    ico: '📈' },
  { key: 'reports',  label: 'Intel Reports',ico: '📄' },
  { key: 'coeus',    label: 'Coeus',        ico: '◉' },
];

const MOBILE_NAV = ['games', 'threats', 'matchup', 'context', 'coeus'];

function fiShell({ page, pageLabel, status = 'ready' }) {
  document.body.dataset.page = page;

  const item = n => {
    const active = n.key === page ? ' active' : '';
    const soon = n.href ? '' : '<span class="soon">SOON</span>';
    const tag = n.href ? 'a' : 'button';
    const attr = n.href ? ` href="${n.href}"` : ' type="button" disabled';
    return `<${tag} class="nav-item${active}"${attr}>
      <span class="nav-ico">${n.ico}</span>${n.label}${soon}</${tag}>`;
  };

  const mobileItem = key => {
    const n = NAV.find(x => x.key === key);
    const active = n.key === page ? ' active' : '';
    const tag = n.href ? 'a' : 'button';
    const attr = n.href ? ` href="${n.href}"` : ' type="button" disabled';
    return `<${tag} class="mobile-nav-btn${active}"${attr}>
      <span class="mnav-icon">${n.ico}</span>${n.label.split(' ')[0]}</${tag}>`;
  };

  document.body.insertAdjacentHTML('afterbegin', `
    <header>
      <div class="header-left">
        <button class="sidebar-toggle" id="fiSidebarToggle" aria-label="Open menu">☰</button>
        <div class="logo"><span class="logo-main">FOOTBALL <span>INTEL</span></span></div>
        <span class="page-label">${pageLabel}</span>
      </div>
      <div class="header-right">
        <span class="last-updated" id="fiUpdated"></span>
        <span class="live-dot ${status === 'ready' ? '' : status}" id="fiStatus">${status === 'ready' ? 'Ready' : status}</span>
        <button class="theme-toggle" id="fiTheme" title="Toggle light and dark mode">🌙</button>
      </div>
    </header>
    <div class="sidebar-overlay" id="fiOverlay"></div>
    <div class="shell">
      <aside class="sidebar" id="fiSidebar">
        <div class="sidebar-mobile-header">
          <span class="logo-main">FOOTBALL <span>INTEL</span></span>
          <button class="icon-btn" id="fiSidebarClose" aria-label="Close menu">✕</button>
        </div>
        <div class="sidebar-section">
          <div class="sidebar-section-title">Dashboard</div>
          ${NAV.map(item).join('')}
        </div>
      </aside>
      <main id="fiMain"></main>
    </div>
    <nav class="mobile-bottom-nav">
      <div class="mobile-bottom-nav-inner">${MOBILE_NAV.map(mobileItem).join('')}</div>
    </nav>
  `);

  // theme
  const saved = localStorage.getItem('fi_theme');
  if (saved === 'light') document.body.classList.add('light-mode');
  const syncIcon = () =>
    document.getElementById('fiTheme').textContent =
      document.body.classList.contains('light-mode') ? '☀️' : '🌙';
  syncIcon();
  document.getElementById('fiTheme').addEventListener('click', () => {
    document.body.classList.toggle('light-mode');
    localStorage.setItem('fi_theme',
      document.body.classList.contains('light-mode') ? 'light' : 'dark');
    syncIcon();
  });

  // sidebar (mobile)
  const sb = document.getElementById('fiSidebar');
  const ov = document.getElementById('fiOverlay');
  const toggle = () => { sb.classList.toggle('open'); ov.classList.toggle('open'); };
  document.getElementById('fiSidebarToggle').addEventListener('click', toggle);
  document.getElementById('fiSidebarClose').addEventListener('click', toggle);
  ov.addEventListener('click', toggle);

  return document.getElementById('fiMain');
}

function fiStatus(text, kind) {
  const el = document.getElementById('fiStatus');
  el.textContent = text;
  el.className = 'live-dot' + (kind ? ' ' + kind : '');
}
function fiUpdated(text) { document.getElementById('fiUpdated').textContent = text; }

/* ── THREAT TIERS (shared by threats.html and games.html) ──────────────
   Buckets are exclusive and a category is consumed by the tightest tier
   that claims it. Within a tier: 1 convergence = Double, 1 convergence
   plus another qualifying strength = Triple, 2+ convergences = Quadruple. */
const FI_TIERS = [
  { key: 'nuclear',  label: 'Nuclear',  playerMax: 3,  defMin: 30 },
  { key: 'elite',    label: 'Elite',    playerMax: 5,  defMin: 28 },
  { key: 'standard', label: 'Standard', playerMax: 10, defMin: 23 },
];

function fiClassify(cats){
  const assigned = {};
  for (const [cat, c] of Object.entries(cats || {})){
    for (const t of FI_TIERS){
      if (c.r <= t.playerMax && c.dr >= t.defMin){ assigned[cat] = t.key; break; }
    }
  }
  const out = [], used = new Set();
  for (const t of FI_TIERS){
    const conv = Object.keys(assigned).filter(c => assigned[c] === t.key);
    if (!conv.length) continue;
    const extra = Object.entries(cats)
      .filter(([c, v]) => !conv.includes(c) && !used.has(c) && v.r <= t.playerMax)
      .map(([c]) => c);
    conv.forEach(c => used.add(c));
    extra.forEach(c => used.add(c));
    out.push({ tier: t.key, tierLabel: t.label,
               type: conv.length >= 2 ? 'Quadruple' : (extra.length ? 'Triple' : 'Double'),
               conv, extra });
  }
  return out;
}

/* ── TEAM LOGOS ──────────────────────────────────────────────────────
   ESPN's CDN, keyed by their abbreviations. Only two differ from
   nflverse's: the Rams and Washington. */
const FI_ESPN_ABBR = { LA: 'lar', WAS: 'wsh' };
/* Preload the two logos most pages show first so they don't pop in late. */
function fiPreloadLogos(teams){
  (teams || []).slice(0, 8).forEach(t => { const i = new Image(); i.src = fiLogo(t); });
}
function fiLogo(team){
  const a = (FI_ESPN_ABBR[team] || team || '').toLowerCase();
  return `https://a.espncdn.com/i/teamlogos/nfl/500/${a}.png`;
}
/* Renders a logo that quietly falls back to the abbreviation if the
   image can't load, so the page never shows a broken icon. */
function fiLogoHTML(team, size){
  const px = size || 30;
  return `<span class="fi-logo" style="width:${px}px;height:${px}px">
    <img src="${fiLogo(team)}" alt="${team}" width="${px}" height="${px}"
         loading="lazy" onerror="this.style.display='none';this.parentNode.classList.add('fallback')">
    <i>${team}</i></span>`;
}

/* rank tier → pill class (1-8 elite … 25-32 poor) */
function rkClass(r) { return r <= 8 ? 't1' : r <= 16 ? 't2' : r <= 24 ? 't3' : 't4'; }
function esc(s) { const d = document.createElement('div'); d.textContent = s ?? ''; return d.innerHTML; }
