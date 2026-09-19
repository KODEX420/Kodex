document.addEventListener("DOMContentLoaded", () => {

    const button = document.getElementById("enterBtn");
    const popup = document.getElementById("voidPopup");
    const closeBtn = document.getElementById("closeBtn");

    button.addEventListener("click", () => {
        popup.style.display = "flex";
    });

    closeBtn.addEventListener("click", () => {
        popup.style.display = "none";
    });

});