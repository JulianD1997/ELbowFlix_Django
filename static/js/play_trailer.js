const overlay = document.querySelector('.overlay__video')
const playButtons = document.querySelectorAll('.play__button')
const closeButton = document.querySelector('.close__button')
const trailerContainer = document.createElement('div')
let iframe = null

playButtons.forEach(playButton => {
  playButton.addEventListener("click", async (event) => {
    event.stopPropagation();
    try {
      const movieId = parseInt(playButton.dataset.movieId)
      const response = await fetch(`./movie/${movieId}/`)
      const data = await response.json()
      overlay.classList.add('open')
      trailerContainer.innerHTML = `
        <iframe 
          class="video" 
          src="https://www.youtube.com/embed/${data.key}?autoplay=0&rel=0" 
          title="${data.name}" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen>
        </iframe>`
      overlay.appendChild(trailerContainer)
      iframe = overlay.querySelector(".video")
    } catch (error) {
      console.error(error)
    }
  })
})

function removeOverlay() {
  overlay.classList.remove('open')
  iframe.remove()
  iframe = null
  console.clear()
}

closeButton.addEventListener('click', removeOverlay)
window.addEventListener('click', (e) => {
  if (e.target == overlay) removeOverlay()
})