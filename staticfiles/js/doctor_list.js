var prevButton = document.getElementById('prev-btn');
var nextButton = document.getElementById('next-btn');
var pageButtons = document.querySelectorAll('.page-number');

var currentPage = 1;
var totalPages = pageButtons.length;

prevButton.addEventListener('click', handlePrevClick);
nextButton.addEventListener('click', handleNextClick);

function handlePrevClick() {
  if (currentPage > 1) {
    currentPage--;
    updatePagination();
    console.log('Previous button clicked');
    // Implement logic to update page content
  }
}

function handleNextClick() {
  if (currentPage < totalPages) {
    currentPage++;
    updatePagination();
    console.log('Next button clicked');
    // Implement logic to update page content
  }
}

function updatePagination() {
  pageButtons.forEach(function(button) {
    if (button.textContent == currentPage) {
      button.classList.add('active');
    } else {
      button.classList.remove('active');
    }
  });
}
