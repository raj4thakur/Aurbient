document.addEventListener("DOMContentLoaded", function() {
    function revealOnScroll() {
        let elements = document.querySelectorAll('.about-container, .vision-container, .testimonial-section');
        let windowHeight = window.innerHeight;

        elements.forEach(el => {
            let position = el.getBoundingClientRect().top;
            if (position < windowHeight - 100) {
                el.classList.add("visible");
            }
        });
    }

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll(); // Run once on load
});
