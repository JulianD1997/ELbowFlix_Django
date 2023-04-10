const carouselTrending = document.querySelector('.carousel__trending')
const carouselUpcoming = document.querySelector('.carousel__upcoming')
const carouselGlobal = document.querySelector('.carousel__global')
const rightButton = document.querySelector('.button.right')
const leftButton = document.querySelector('.button.left')

async function getTrendingMovies() {
  const response = await fetch('./movie/?resource=trending/movie&type_=day')
  const data = await response.json()
  data.forEach((movie) => {
    carouselTrending.innerHTML += `
      <div class='card__flex'>
        <img class='card__flex-img' src="${movie.poster}" alt="${movie.title}">
        <div class='card__flex-container'>
          <h4 class='card__flex-title'>${movie.title}</h4>
        </div>
      </div>
    `
  })
}

async function getUpcomingMovies() {
  const response = await fetch(`./movie/?resource=movie&type_=upcoming&region=ES`)
  const data = await response.json()
  data.forEach((movie) => {
    carouselUpcoming.innerHTML += `
      <div class='card__flex'>
        <img class='card__flex-img' src="${movie.poster}" alt="${movie.title}">
        <div class='card__flex-container'>
          <h4 class='card__flex-title'>${movie.title}</h4>
        </div>
      </div>
    `
  })
}

leftButton.addEventListener('click', () => {
    carouselGlobal.scrollLeft = carouselGlobal.scrollLeft - 340
})

rightButton.addEventListener('click', () => {
    carouselGlobal.scrollLeft = carouselGlobal.scrollLeft + 340
})

getTrendingMovies()
getUpcomingMovies()