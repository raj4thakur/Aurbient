document.addEventListener("DOMContentLoaded", function () {
    const serviceCards = document.querySelectorAll(".service-card");
    serviceCards.forEach(card => {
        const imageUrl = card.getAttribute("data-image");
        if (imageUrl) {
            card.style.setProperty("--hover-bg", `url('${imageUrl}')`);
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const formContainer = document.getElementById("serviceForm");
    const openFormBtn = document.getElementById("openFormBtn");
    const closeFormBtn = document.getElementById("closeFormBtn");

    openFormBtn.addEventListener("click", function () {
        formContainer.classList.add("show");
    });

    closeFormBtn.addEventListener("click", function () {
        formContainer.classList.remove("show");
    });

    // Close form when clicking outside of it
    window.addEventListener("click", function (event) {
        if (event.target === formContainer) {
            formContainer.classList.remove("show");
        }
    });
});