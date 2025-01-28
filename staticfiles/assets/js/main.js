(function () {
  "use strict";

  // Função para selecionar elementos
  const select = (el, all = false) => {
    el = el.trim();
    return all ? [...document.querySelectorAll(el)] : document.querySelector(el);
  };

  // Função para adicionar ouvintes de eventos
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener));
      } else {
        selectEl.addEventListener(type, listener);
      }
    }
  };

  // Função para atualizar o estilo de elementos
  const updateElementStyle = (elementId, iconId, isAtBottom) => {
    const element = document.getElementById(elementId);
    const icon = document.getElementById(iconId);

    if (isAtBottom) {
      icon.style.color = '#cb916b';
      element.style.backgroundColor = '#fff';
    } else {
      icon.style.color = '#fff';
      element.style.backgroundColor = '#cb916b';
    }
  };

  // Evento de scroll
  window.addEventListener('scroll', function () {
    const windowHeight = window.innerHeight;
    const scrollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;

    if (window.innerWidth <= 1200 && (scrollPosition + windowHeight) >= document.body.offsetHeight) {
      updateElementStyle('id_button', 'id_icon', true);  // Quando estiver na parte inferior
    } else {
      updateElementStyle('id_button', 'id_icon', false);  // Quando não estiver
    }
  });

  /** 
   * Função para lidar com eventos de scroll para links da barra de navegação
   */
  const handleScrollEvent = () => {
    let navbarlinks = select('#navbar .scrollto', true);
    let position = window.scrollY + 200;

    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return;

      let section = select(navbarlink.hash);
      if (section) {
        if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
          navbarlink.classList.add('active');
        } else {
          navbarlink.classList.remove('active');
        }
      }
    });
  };

  // Configuração inicial de scroll
  window.addEventListener('load', handleScrollEvent);
  on('scroll', document, handleScrollEvent);

  // Função de rolar até o elemento com offset
  const scrollto = (el) => {
    let elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos,
      behavior: 'smooth'
    });
  };

  // Botão "voltar ao topo"
  let backtotop = select('.back-to-top');
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active');
      } else {
        backtotop.classList.remove('active');
      }
    };
    window.addEventListener('load', toggleBacktotop);
    on('scroll', document, toggleBacktotop);
  }

  // Alternar navegação móvel
  on('click', '.mobile-nav-toggle', function (e) {
    select('body').classList.toggle('mobile-nav-active');
    this.classList.toggle('bi-list');
    this.classList.toggle('bi-x');
  });

  // Rolar para o elemento ao clicar no link
  on('click', '.scrollto', function (e) {
    if (select(this.hash)) {
      e.preventDefault();
      let body = select('body');
      if (body.classList.contains('mobile-nav-active')) {
        body.classList.remove('mobile-nav-active');
        let navbarToggle = select('.mobile-nav-toggle');
        navbarToggle.classList.toggle('bi-list');
        navbarToggle.classList.toggle('bi-x');
      }
      scrollto(this.hash);
    }
  }, true);

  // Rolar para o elemento na inicialização se houver hash na URL
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash);
      }
    }
  });

  // Efeito de digitação
  const typed = select('.typed');
  if (typed) {
    let typed_strings = typed.getAttribute('data-typed-items');
    typed_strings = typed_strings.split(',');
    new Typed('.typed', {
      strings: typed_strings,
      loop: true,
      typeSpeed: 100,
      backSpeed: 50,
      backDelay: 2000
    });
  }

  // Animação de habilidades
  let skilsContent = select('.skills-content');
  if (skilsContent) {
    new Waypoint({
      element: skilsContent,
      offset: '80%',
      handler: function (direction) {
        let progress = select('.progress .progress-bar', true);
        progress.forEach((el) => {
          el.style.width = el.getAttribute('aria-valuenow') + '%';
        });
      }
    });
  }

  // Portfolio e filtros
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });
      let portfolioFilters = select('#portfolio-flters li', true);
      on('click', '#portfolio-flters li', function (e) {
        e.preventDefault();
        portfolioFilters.forEach(function (el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');
        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function () {
          AOS.refresh();
        });
      }, true);
    }
  });

  // Lightbox do portfólio
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  // Slider de detalhes do portfólio
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  // Slider de depoimentos
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  // Animação ao rolar a página
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  });

  // Contador Pure Counter
  new PureCounter();

})();
