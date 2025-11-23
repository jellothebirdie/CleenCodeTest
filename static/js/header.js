const headerContainer = document.querySelector('.header-container');
let lastScrollY = window.scrollY;

function handleScroll() {
    const currentScrollY = window.scrollY;
    const headerImage = document.querySelector('.header-image');
    const imageHeight = headerImage.offsetHeight;
    
    // Calculate opacity based on scroll position
    // Fade out as you scroll from 0 to imageHeight
    let opacity = 1 - (currentScrollY / imageHeight);
    
    // Clamp opacity between 0 and 1
    opacity = Math.max(0, Math.min(1, opacity));
    
    // Apply the gradual opacity
    headerContainer.style.opacity = opacity;
    
    // Disable pointer events when fully faded
    if (opacity === 0) {
        headerContainer.style.pointerEvents = 'none';
    } else {
        headerContainer.style.pointerEvents = 'auto';
    }
    
    lastScrollY = currentScrollY;
}
  
  // Throttle scroll events for better performance
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        handleScroll();
        ticking = false;
      });
      ticking = true;
    }
  });