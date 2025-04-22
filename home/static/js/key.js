document.addEventListener("keydown", function(event) {
    if (event.key === "a" && event.key === "d" && event.key === "m") {
        let adminUrl = document.getElementById("admin-url").getAttribute("data-url");
        window.location.href = adminUrl;
    }
});