
function toggleHiddenElements(id) {
    let hiddenElement = document.getElementById(id);

    hiddenElement.classList.toggle('hidden');
}

/* CARD EVENT PREVIEW */
var swiper = new Swiper('.blog-slider', {
    spaceBetween: 30,
    effect: 'fade',
    loop: true,
    mousewheel: {
      invert: false,
    },
    // autoHeight: true,
    pagination: {
      el: '.blog-slider__pagination',
      clickable: true,
    }
  });   


  