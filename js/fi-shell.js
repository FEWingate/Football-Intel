/* ═══════════════════════════════════════════════════════════════
   FOOTBALL INTEL — shared shell
   Renders header, sidebar nav, mobile nav and theme handling so
   every page inherits the same chrome. Add a page by appending to
   NAV below and setting <body data-page="key">.
   ═══════════════════════════════════════════════════════════════ */

const NAV = [
  { key: 'threats',  label: 'Threats',      ico: '⚡', href: 'index.html' },
  { key: 'matchup',  label: 'Matchup Stats',ico: '⚔️', href: 'matchup_stats.html' },
  { key: 'context',  label: 'Contextual',   ico: '📊', href: 'contextual_stats.html' },
  { key: 'games',    label: 'Games',        ico: '📅' },
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

const MOBILE_NAV = ['threats', 'matchup', 'context', 'dfs', 'coeus'];

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

/* rank tier → pill class (1-8 elite … 25-32 poor) */
function rkClass(r) { return r <= 8 ? 't1' : r <= 16 ? 't2' : r <= 24 ? 't3' : 't4'; }
function esc(s) { const d = document.createElement('div'); d.textContent = s ?? ''; return d.innerHTML; }
