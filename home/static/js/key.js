document.addEventListener("keydown", function(event) {
    if (event.ctrlKey && event.shiftKey && event.key === "A") {
        let adminUrl = document.getElementById("admin-url").getAttribute("data-url");
        window.location.href = adminUrl;
    }
});