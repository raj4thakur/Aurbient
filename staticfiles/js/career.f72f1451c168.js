document.addEventListener("DOMContentLoaded", function () {
    const applyBtn = document.getElementById("apply-btn"); // Apply Now button
    const applyFormContainer = document.getElementById("apply-form-container"); // Form Container
    const closeBtn = document.getElementById("close-btn"); // Close button

    if (applyBtn && applyFormContainer && closeBtn) {
        // Show the form when "Apply Now" is clicked
        applyBtn.addEventListener("click", function () {
            console.log("Apply Now Clicked!"); // Debugging
            applyFormContainer.style.right = "0"; 
        });

        // Hide the form when "Close" button is clicked
        closeBtn.addEventListener("click", function () {
            console.log("Close Button Clicked!"); // Debugging
            applyFormContainer.style.right = "-400px"; 
        });
    } else {
        console.log("Error: Elements not found in DOM!"); // Debugging
    }
});
