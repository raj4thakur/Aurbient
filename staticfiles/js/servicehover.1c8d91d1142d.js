document.addEventListener("DOMContentLoaded", function () {
    const serviceCards = document.querySelectorAll(".service-card");
    serviceCards.forEach(card => {
        const imageUrl = card.getAttribute("data-image");
        if (imageUrl) {
            card.style.setProperty("--hover-bg", `url('${imageUrl}')`);
        }
    });
});
