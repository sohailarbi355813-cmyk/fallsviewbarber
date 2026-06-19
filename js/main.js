/* =============================================
   INdustry CUTS — Main JavaScript
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {
  initCursor();
  initScrollProgress();
  initNavbar();
  initMobileMenu();
  initScrollReveal();
  initTestimonials();
  initBackToTop();
  initPageTransitions();
  initLightbox();
  initParallax();
});

/* === Custom Cursor === */
function initCursor() {
  const cursor = document.querySelector('.cursor');
  const ring = document.querySelector('.cursor-ring');
  if (!cursor || !ring) return;

  let mx = 0, my = 0, rx = 0, ry = 0;

  document.addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    cursor.style.left = mx + 'px';
    cursor.style.top  = my + 'px';
  });

  // Ring follows with lag
  function animateRing() {
    rx += (mx - rx) * 0.12;
    ry += (my - ry) * 0.12;
    ring.style.left = rx + 'px';
    ring.style.top  = ry + 'px';
    requestAnimationFrame(animateRing);
  }
  animateRing();

  // Hover effects on interactive elements
  const hoverEls = document.querySelectorAll('a, button, .service-card, .portfolio-item, .team-card, .owner-card, .t-dot, #back-to-top, .lb-close, .lb-prev, .lb-next');
  hoverEls.forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.classList.add('hover');
      ring.classList.add('hover');
    });
    el.addEventListener('mouseleave', () => {
      cursor.classList.remove('hover');
      ring.classList.remove('hover');
    });
  });

  document.addEventListener('mouseleave', () => { cursor.style.opacity = '0'; ring.style.opacity = '0'; });
  document.addEventListener('mouseenter', () => { cursor.style.opacity = '1'; ring.style.opacity = '1'; });
}

/* === Scroll Progress Bar === */
function initScrollProgress() {
  const bar = document.getElementById('scroll-progress');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const total = document.body.scrollHeight - window.innerHeight;
    bar.style.width = (scrolled / total * 100) + '%';
  }, { passive: true });
}

/* === Navbar === */
function initNavbar() {
  const nav = document.getElementById('navbar');
  if (!nav) return;

  // Set active link
  const current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href') || '';
    if (href === current || (current === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });
}

/* === Mobile Menu === */
function initMobileMenu() {
  const hamburger = document.querySelector('.hamburger');
  const menu = document.querySelector('.mobile-menu');
  if (!hamburger || !menu) return;

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    menu.classList.toggle('open');
    document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : '';
  });

  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('open');
      menu.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
}

/* === Scroll Reveal (Intersection Observer) === */
function initScrollReveal() {
  const targets = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, [data-stagger]');
  if (!targets.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = el.dataset.delay || 0;
        setTimeout(() => el.classList.add('revealed'), delay);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

  targets.forEach(el => observer.observe(el));
}

/* === Testimonials Carousel === */
function initTestimonials() {
  const track = document.querySelector('.testimonials-track');
  const dotsContainer = document.querySelector('.testimonial-dots');
  if (!track) return;

  const slides = track.querySelectorAll('.testimonial-slide');
  if (slides.length < 2) return;

  let current = 0;
  let timer = null;
  let isHovered = false;

  // Build dots
  if (dotsContainer) {
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = 't-dot' + (i === 0 ? ' active' : '');
      dot.setAttribute('aria-label', `Slide ${i + 1}`);
      dot.addEventListener('click', () => goTo(i));
      dotsContainer.appendChild(dot);
    });
  }

  function updateDots() {
    if (!dotsContainer) return;
    dotsContainer.querySelectorAll('.t-dot').forEach((d, i) => {
      d.classList.toggle('active', i === current);
    });
  }

  function goTo(index) {
    current = (index + slides.length) % slides.length;
    track.style.transform = `translateX(-${current * 100}%)`;
    updateDots();
  }

  function next() { goTo(current + 1); }

  function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => { if (!isHovered) next(); }, 5000);
  }

  track.closest('.testimonials-section')?.addEventListener('mouseenter', () => isHovered = true);
  track.closest('.testimonials-section')?.addEventListener('mouseleave', () => isHovered = false);

  // Touch / swipe
  let touchStartX = 0;
  track.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) goTo(current + (diff > 0 ? 1 : -1));
  });

  startTimer();
}

/* === Back to Top === */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 500);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* === Page Transitions === */
function initPageTransitions() {
  const overlay = document.querySelector('.page-transition');
  if (!overlay) return;

  // Fade in on load
  overlay.classList.remove('active');

  document.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('mailto') || href.startsWith('tel') || href.startsWith('http')) return;

    link.addEventListener('click', e => {
      e.preventDefault();
      overlay.classList.add('active');
      setTimeout(() => { window.location.href = href; }, 380);
    });
  });
}

/* === Lightbox === */
function initLightbox() {
  const lb = document.getElementById('lightbox');
  if (!lb) return;

  const lbImg = lb.querySelector('.lb-img');
  const lbClose = lb.querySelector('.lb-close');
  const lbPrev = lb.querySelector('.lb-prev');
  const lbNext = lb.querySelector('.lb-next');

  const items = [...document.querySelectorAll('.portfolio-item[data-src]')];
  let current = 0;

  function open(index) {
    current = index;
    lbImg.src = items[current].dataset.src;
    lbImg.alt = items[current].dataset.caption || '';
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function close() {
    lb.classList.remove('open');
    document.body.style.overflow = '';
    setTimeout(() => { lbImg.src = ''; }, 350);
  }

  function prev() { current = (current - 1 + items.length) % items.length; lbImg.src = items[current].dataset.src; }
  function next() { current = (current + 1) % items.length; lbImg.src = items[current].dataset.src; }

  items.forEach((item, i) => item.addEventListener('click', () => open(i)));
  lbClose?.addEventListener('click', close);
  lbPrev?.addEventListener('click', prev);
  lbNext?.addEventListener('click', next);
  lb.addEventListener('click', e => { if (e.target === lb) close(); });

  document.addEventListener('keydown', e => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') prev();
    if (e.key === 'ArrowRight') next();
  });
}

/* === Parallax on hero === */
function initParallax() {
  const heroBgs = document.querySelectorAll('.hero-bg, .page-hero-bg');
  if (!heroBgs.length) return;

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    heroBgs.forEach(bg => {
      bg.style.transform = `scale(1) translateY(${scrollY * 0.25}px)`;
    });
  }, { passive: true });
}

/* === Number counter animation === */
function animateCounters() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const target = +el.dataset.count;
    const duration = 1800;
    const start = performance.now();
    function step(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target) + (el.dataset.suffix || '');
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });
}

// Trigger counter when awards section enters view
const awardsSection = document.querySelector('.awards-section');
if (awardsSection) {
  new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) { animateCounters(); }
  }, { threshold: 0.3 }).observe(awardsSection);
}
