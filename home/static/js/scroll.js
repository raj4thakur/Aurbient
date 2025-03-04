
const scrollLeftButton = document.getElementById('scroll-left');
const scrollRightButton = document.getElementById('scroll-right');
const scrollableContent = document.getElementById('scrollable-content');

scrollLeftButton.addEventListener('click', () => {
scrollableContent.scrollBy({ left: -300, behavior: 'smooth' });
});

scrollRightButton.addEventListener('click', () => {
scrollableContent.scrollBy({ left: 300, behavior: 'smooth' });
});
