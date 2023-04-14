const burger = document.querySelector('#burger');
const navMenu = document.querySelector('.nav__menu');

burger.addEventListener('click', () => {
  // toggle the 'active' class on both the burger and the nav menu
  if (burger.classList.contains('active')) {
    burger.classList.remove('active');
    burger.classList.add('no_active');
    navMenu.classList.remove('active');
  } else {
    burger.classList.remove('no_active');
    burger.classList.add('active');
    navMenu.classList.add('active');
  }
})
document.querySelectorAll('.nav__link').forEach(n =>
    n.addEventListener('click', () => {
        burger.classList.remove('active');
        navMenu.classList.remove('active');
    })
)