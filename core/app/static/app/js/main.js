const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
};






  const search = document.querySelector('.container-search');
  const input = document.querySelector('.input-search');
  const btn  = document.querySelector('.btn');
  
  btn.addEventListener('click', () => {
      search.classList.toggle('active')
      input.focus()
  })
  