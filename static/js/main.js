function toggleMenu() {
  const m = document.getElementById('mobileMenu');
  m.classList.toggle('open');
}

document.addEventListener('click', function(e) {
  const m = document.getElementById('mobileMenu');
  const h = document.getElementById('hamburger');
  if (m && h && !m.contains(e.target) && !h.contains(e.target)) {
    m.classList.remove('open');
  }
});

fetch('/api/stats')
  .then(r => r.json())
  .then(d => {
    const a = document.getElementById('statActive');
    const c = document.getElementById('statClosed');
    const u = document.getElementById('statUsers');
    const fs = document.getElementById('footerStats');
    if (a) a.textContent = d.active;
    if (c) c.textContent = d.closed;
    if (u) u.textContent = d.users;
    if (fs) fs.textContent = d.active + ' active items · ' + d.closed + ' reunited · ' + d.users + ' students · ' + d.reachouts + ' reach-outs';
  })
  .catch(() => {});

setTimeout(function() {
  document.querySelectorAll('.flash-msg').forEach(el => {
    el.style.transition = 'opacity 0.5s';
    el.style.opacity = '0';
    setTimeout(() => el.remove(), 500);
  });
}, 4000);
