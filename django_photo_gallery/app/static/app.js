'use strict'

// Initializes the swiper menu 
var swiperMenuInit = function() {
    var menuButton = document.querySelector('.menu-button');
    var swiper = new Swiper('.swiper-menu', {
      slidesPerView: 'auto',
      initialSlide: 1,
      resistanceRatio: 0,
      slideToClickedSlide: true,
      on: {
        init: function () {
          var slider = this;
          menuButton.addEventListener('click', function () {
            if (slider.activeIndex === 0) {
              slider.slideNext();
            } else {
              slider.slidePrev();
            }
          }, true);
        },
        slideChange: function () {
          var slider = this;
          if (slider.activeIndex === 0) {
            menuButton.classList.add('cross');
          } else {
            menuButton.classList.remove('cross');
          }
        },
      }
    });
}

// Initializes the home page slider
var homeSliderInit = function () {
    new Swiper('.swiper-container', {
        speed: 600,
        parallax: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        }
      });
}

// Initializes PhotoSwipe.
var pswpInit = function (startsAtIndex) {

    if (!startsAtIndex) {
        startsAtIndex = 0;
    }

    var pswpElement = document.querySelectorAll('.pswp')[0];

    // commented the array bellow since the images array will be loaded from the server
    // in variable called djangoAlbumImages.

    // build items array
    //var items = [
    //    {
    //        src: 'https://placekitten.com/600/400',
    //        w: 600,
    //        h: 400
    //    },
    //    {
    //        src: 'https://placekitten.com/1200/900',
    //        w: 1200,
    //        h: 900
    //    }
    //];

    // find is images are loaded from the server.
    if (window.djangoAlbumImages && window.djangoAlbumImages.length > 0) {
        // define options (if needed)
        var options = {
            // optionName: 'option value'
            // for example:
            index: startsAtIndex // start at first slide
        };

        // Initializes and opens PhotoSwipe
        var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, window.djangoAlbumImages, options);
        gallery.init();
    }
}

document.addEventListener("DOMContentLoaded", function(){
    swiperMenuInit();
    homeSliderInit();
});
