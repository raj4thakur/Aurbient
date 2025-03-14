document.addEventListener("DOMContentLoaded", function () {
    const applyBtn = document.getElementById("apply-btn");
    const applyForm = document.getElementById("apply-form-container");
    const closeBtn = document.getElementById("close-btn");

    // Show the form when "Apply Now" is clicked
    applyBtn.addEventListener("click", function () {
        applyForm.style.right = "0"; // Slide in
    });

    // Hide the form when "✖" is clicked
    closeBtn.addEventListener("click", function () {
        applyForm.style.right = "-400px"; // Slide out
    });

    // Close form when clicking outside of it
    window.addEventListener("click", function (e) {
        if (e.target === applyForm) {
            applyForm.style.right = "-400px";
        }
    });
});
