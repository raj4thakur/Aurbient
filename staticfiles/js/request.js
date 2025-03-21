document.addEventListener("DOMContentLoaded", function() {
    const openButtons = document.querySelectorAll(".open-form-btn"); // All CTA buttons
    const formContainer = document.getElementById("serviceForm"); // Sliding form
    const closeFormBtn = document.getElementById("closeFormBtn"); // Close button

    // Open form when any CTA button is clicked
    openButtons.forEach(button => {
        button.addEventListener("click", function() {
            formContainer.classList.add("active");
        });
    });

    // Close form when close button is clicked
    closeFormBtn.addEventListener("click", function() {
        formContainer.classList.remove("active");
    });

    // Close form when clicking outside the form
    document.addEventListener("click", function(event) {
        if (!formContainer.contains(event.target) && !event.target.classList.contains("open-form-btn")) {
            formContainer.classList.remove("active");
        }
    });
});
