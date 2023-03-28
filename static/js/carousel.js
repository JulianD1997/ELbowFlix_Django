//--------------------Carrusel--------------------

const carousel = document.querySelector('.carousel__container')
const leftButton = document.querySelector('.move__button.left')
const rightButton = document.querySelector('.move__button.right')

// variables
//todas las tarjetas
let cards = document.querySelectorAll('.card')
let interval = null
//ultima tarjeta del carrusel
let sliderCardLast = cards[cards.length - 1]

//agregar la ultima tarjeta al comienzo
carousel.insertAdjacentElement('afterbegin', sliderCardLast)

// Mueve las tarjetas hacia la derecha
function moveCardsNext() {
    let sliderCardFirst = document.querySelectorAll('.card')[0]
    carousel.style.marginLeft = '-200%'
    carousel.style.transition = 'margin-left 800ms ease-out'
    setTimeout(function(){
        carousel.style.transition = 'none'
        carousel.insertAdjacentElement('beforeend',sliderCardFirst)
        carousel.style.marginLeft = '-100%'
    },800)
}
// Mueve las tarjetas hacia la izquierda
function moveCardsPrev() {
    let cards = document.querySelectorAll('.card')
    let sliderCardLast = cards[cards.length - 1]
    carousel.style.marginLeft = '0'
    carousel.style.transition = 'margin-left 800ms ease-out'
    setTimeout(function(){
        carousel.style.transition = 'none'
        carousel.insertAdjacentElement('afterbegin', sliderCardLast)
        carousel.style.marginLeft = '-100%'
    },800)
}

// Agrega listeners a los botones para mover las tarjetas
rightButton.addEventListener('click',moveCardsNext)
leftButton.addEventListener('click',moveCardsPrev)

// Funciones para el slider automático
const autoSlider = () => interval = setInterval(moveCardsNext,3000)
const stopSlider = () => {
  clearInterval(interval)
  return null
}

// Detiene el slider al pasar el cursor sobre el carrusel
carousel.addEventListener('mouseover',()=> {
  interval = stopSlider()
})
carousel.addEventListener('mouseout',()=> {
  interval=autoSlider()
})
autoSlider()

