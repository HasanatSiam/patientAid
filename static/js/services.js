const welcomeText = document.getElementById('welcome-text');

gsap.from(welcomeText, {
  opacity: 0, // Start with 0 opacity
  y: 50, // Move down 50 pixels
  duration: 1, // Animation duration in seconds
  ease: 'power2.out' // Easing function
});

document.addEventListener('DOMContentLoaded', () => {
    // Your GSAP animation code here
  });



  function initMap() {
    var mapContainer = document.getElementById('map');
  
    var iframe = document.createElement('iframe');
    iframe.setAttribute('src', 'https://www.google.com/maps/embed?pb=!1m18...'); // Replace with your Google Maps embed URL
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('aria-hidden', 'false');
    iframe.setAttribute('tabindex', '0');
  
    mapContainer.appendChild(iframe);
  }

  initMap();



  // Add interactivity to the navigation links
const navigationLinks = document.querySelectorAll('.navigation-links a');

navigationLinks.forEach(link => {
  link.addEventListener('click', function(event) {
    event.preventDefault();
    const targetSectionId = link.getAttribute('href');
    const targetSection = document.querySelector(targetSectionId);
    targetSection.scrollIntoView({ behavior: 'smooth' });
  });
});


  





  
