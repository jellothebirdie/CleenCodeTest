const headerImage = document.querySelector('.header-image');
let lastScrollY = window.scrollY;

function handleScroll() {
    const currentScrollY = window.scrollY;
    const imageHeight = headerImage.offsetHeight;
    
    // Calculate opacity based on scroll position
    // Fade out as you scroll from 0 to imageHeight
    let opacity = 1 - (currentScrollY / imageHeight);
    
    // Clamp opacity between 0 and 1
    opacity = Math.max(0, Math.min(1, opacity));
    
    // Apply the gradual opacity
    headerImage.style.opacity = opacity;
    
    // Disable pointer events when fully faded
    if (opacity === 0) {
        headerImage.style.pointerEvents = 'none';
    } else {
        headerImage.style.pointerEvents = 'auto';
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