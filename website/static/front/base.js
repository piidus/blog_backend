// Toggle menu on mobile view
// Toggle the dropdown menu visibility
function toggleMenu() {
  const navbarLinks = document.getElementById("navbar-links");
  navbarLinks.classList.toggle("active");
}

// Close the dropdown if clicked outside
document.addEventListener("click", function(event) {
  const navbarLinks = document.getElementById("navbar-links");
  const hamburger = document.querySelector(".hamburger");

  // Check if the click is outside the dropdown and hamburger menu
  if (!navbarLinks.contains(event.target) && !hamburger.contains(event.target)) {
    navbarLinks.classList.remove("active");
  }
});
