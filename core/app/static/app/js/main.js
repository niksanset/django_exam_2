const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}


const search = document.querySelector('.container-search');
const input = document.querySelector('.input-search');
const btn  = document.querySelector('.btn');

btn.addEventListener('click', () => {
    search.classList.toggle('active')
    input.focus()
})


document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector('.carousel');
    const carouselInner = carousel.querySelector('.carousel-inner');
    const carouselItems = carousel.querySelectorAll('.carousel-item');
    const prevButton = carousel.querySelector('.prev');
    const nextButton = carousel.querySelector('.next');
    let currentIndex = 0;
    let intervalId;

    function goToSlide(index) {
      carouselInner.style.transform = `translateX(-${index * 100}%)`;
      currentIndex = index;
    }

    function nextSlide() {
      if (currentIndex < carouselItems.length - 1) {
        goToSlide(currentIndex + 1);
      } else {
        goToSlide(0);
      }
    }

    function startAutoPlay() {
      intervalId = setInterval(nextSlide, 5000); // Измените интервал по вашему усмотрению (2000 миллисекунд = 2 секунды)
    }

    function stopAutoPlay() {
      clearInterval(intervalId);
    }

    prevButton.addEventListener('click', function() {
      stopAutoPlay();
      if (currentIndex > 0) {
        goToSlide(currentIndex - 1);
      } else {
        goToSlide(carouselItems.length - 1);
      }
    });

    nextButton.addEventListener('click', function() {
      stopAutoPlay();
      nextSlide();
    });

    carousel.addEventListener('mouseenter', stopAutoPlay);
    carousel.addEventListener('mouseleave', startAutoPlay);

    startAutoPlay(); // Начать автоматическое воспроизведение при загрузке страницы
  });



