// Waterworks Plumbing Qld - Interactive Engine
document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Drawer Navigation
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-menu-drawer');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', () => {
      drawer.classList.toggle('open');
      const isOpen = drawer.classList.contains('open');
      toggleBtn.setAttribute('aria-expanded', isOpen);
    });

    document.addEventListener('click', (e) => {
      if (!drawer.contains(e.target) && !toggleBtn.contains(e.target) && drawer.classList.contains('open')) {
        drawer.classList.remove('open');
      }
    });
  }

  // 2. Dynamic Typewriter Animation
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const words = [
      'Hot Water Specialists',
      '24/7 Emergency Plumbers',
      'Blocked Drain Hydro-Jetting',
      'QBCC Licensed Gasfitters',
      'Brisbane Northside Experts'
    ];
    let wordIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typeSpeed = 90;

    function type() {
      const currentWord = words[wordIndex];
      if (isDeleting) {
        typewriterEl.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
        typeSpeed = 45;
      } else {
        typewriterEl.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
        typeSpeed = 90;
      }

      if (!isDeleting && charIndex === currentWord.length) {
        isDeleting = true;
        typeSpeed = 1600; // Pause at end of word
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        typeSpeed = 400; // Pause before typing new word
      }

      setTimeout(type, typeSpeed);
    }
    type();
  }

  // 3. Animated Number Counters
  const counters = document.querySelectorAll('.stat-number');
  if (counters.length > 0) {
    let animated = false;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
          animated = true;
          counters.forEach(counter => {
            const target = parseInt(counter.getAttribute('data-target'), 10);
            const suffix = counter.getAttribute('data-suffix') || '';
            let count = 0;
            const duration = 1600;
            const stepTime = Math.max(16, duration / target);
            const step = Math.ceil(target / (duration / stepTime));

            const timer = setInterval(() => {
              count += step;
              if (count >= target) {
                counter.textContent = target.toLocaleString() + suffix;
                clearInterval(timer);
              } else {
                counter.textContent = count.toLocaleString() + suffix;
              }
            }, stepTime);
          });
        }
      });
    }, { threshold: 0.3 });

    const statsBanner = document.querySelector('.stats-banner');
    if (statsBanner) {
      observer.observe(statsBanner);
    }
  }

  // 4. Interactive Plumbing Emergency & Hot Water Triage Widget
  initTriageWidget();
});

function initTriageWidget() {
  const triageContainer = document.querySelector('.triage-box');
  if (!triageContainer) return;

  const propertyChips = triageContainer.querySelectorAll('[data-property]');
  const issueChips = triageContainer.querySelectorAll('[data-issue]');
  const resultTitle = document.getElementById('triageTitle');
  const resultDesc = document.getElementById('triageDesc');
  const resultAction = document.getElementById('triageAction');

  let selectedProperty = 'Residential Home';
  let selectedIssue = 'Hot Water Failure';

  const triageData = {
    'Hot Water Failure': {
      title: 'Emergency Hot Water Element / Cylinder Inspection Required',
      desc: 'No hot water or a leaking storage tank requires priority diagnostic by a licensed plumber. We isolate electrical/gas supplies, test pressure relief valves, and provide same-day repair or full energy-efficient unit replacement.',
      action: 'Call 0418 988 181 for Same-Day Hot Water'
    },
    'Burst Pipe / Flooding': {
      title: 'Critical Emergency: Immediate Main Water Shut-Off Needed',
      desc: 'Active water gushing through walls, floors, or yard mains causes severe structural damp. Locate your council water meter at the front boundary and turn the brass cock clockwise. Our mobile rapid-response van is equipped with pipe locating and repair gear.',
      action: 'Call 0418 988 181 for 24/7 Rapid Response'
    },
    'Blocked Drain / Overflow': {
      title: 'High-Pressure Hydro-Jetting & CCTV Camera Survey Recommended',
      desc: 'Gurgling toilet traps, slow-draining showers, or sewer inspection openings overflowing in the yard indicate a main line blockage. We deploy 5000 PSI hydro-jetters to blast tree roots and clear obstructions without trenching.',
      action: 'Schedule Hydro-Jet Drain Clearing'
    },
    'Gas Leak / Smell': {
      title: 'Urgent Safety Hazard: Isolate Gas Bottle or Main Meter Immediately',
      desc: 'Smelling gas or hearing a hiss around appliances or hot water units poses an immediate combustion risk. Turn off gas bottles or the meter valve, extinguish open flames, open windows, and call us immediately for digital manometer testing.',
      action: 'Emergency Gas Line Dispatch: 0418 988 181'
    },
    'Leaking Tap / Toilet': {
      title: 'Preventative Ceramic Disc Sealing & Cistern Valve Overhaul',
      desc: 'A continuously trickling toilet or dripping tap wastes over 20,000 litres of water annually. We replace degraded inlet valves, reseat tap spindles, and install premium water-saving fixtures across Brisbane North.',
      action: 'Book Routine Tap & Valve Service'
    }
  };

  function updateTriage() {
    const data = triageData[selectedIssue] || triageData['Hot Water Failure'];
    if (resultTitle) resultTitle.textContent = `${selectedProperty} — ${data.title}`;
    if (resultDesc) resultDesc.textContent = data.desc;
    if (resultAction) {
      resultAction.textContent = data.action;
      resultAction.href = 'tel:61418988181';
    }
  }

  propertyChips.forEach(chip => {
    chip.addEventListener('click', () => {
      propertyChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      selectedProperty = chip.getAttribute('data-property');
      updateTriage();
    });
  });

  issueChips.forEach(chip => {
    chip.addEventListener('click', () => {
      issueChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      selectedIssue = chip.getAttribute('data-issue');
      updateTriage();
    });
  });
}
