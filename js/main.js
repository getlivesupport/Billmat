document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');

  const setHeaderState = () => {
    if (header) {
      header.classList.toggle('scrolled', window.scrollY > 8);
    }
  };

  const closeMenu = () => {
    if (!toggle || !nav) return;
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  };

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(isOpen));
      if (isOpen) {
        const firstLink = nav.querySelector('a');
        if (firstLink) firstLink.focus();
      }
    });

    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 832) closeMenu();
      });
    });

    document.addEventListener('click', (event) => {
      if (!nav.classList.contains('open')) return;
      if (!(event.target instanceof Node)) return;
      if (nav.contains(event.target) || toggle.contains(event.target)) return;
      closeMenu();
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && nav.classList.contains('open')) {
        closeMenu();
        toggle.focus();
      }
    });
  }

  document.querySelectorAll('.faq-toggle').forEach((button) => {
    const controls = button.getAttribute('aria-controls');
    const panel = controls ? document.getElementById(controls) : null;
    if (!panel) return;

    const syncState = (expanded) => {
      button.setAttribute('aria-expanded', String(expanded));
      panel.hidden = !expanded;
    };

    syncState(button.getAttribute('aria-expanded') === 'true');

    button.addEventListener('click', () => {
      syncState(button.getAttribute('aria-expanded') !== 'true');
    });
  });

  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });
});
