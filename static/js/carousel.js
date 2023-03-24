/* constants */
const carousel = document.querySelector('.carousel__container')
const cards = document.querySelectorAll('.card')
const playButton = document.querySelectorAll('#play__button')

/* variables */
let sliderCardLast = cards[cards.length - 1]

carousel.insertAdjacentElement('afterbegin', sliderCardLast)

function moveCards() {
    let sliderCardFirst = document.querySelectorAll('.card')[0]
    carousel.style.marginLeft = '-200%'
    carousel.style.transition = 'margin-left 800ms ease-out'
    setTimeout(function(){
        carousel.style.transition = 'none'
        carousel.insertAdjacentElement('beforeend',sliderCardFirst)
        carousel.style.marginLeft = '-100%'
    },800)
}
s
setInterval(moveCards,7000)

/* playButton. */