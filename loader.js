window.addEventListener("load", () => {
    const loading = document.getElementById("loading-screen");

    setTimeout(() => {
        loading.style.opacity = "0";

        setTimeout(() => {
            loading.style.display = "none";
        }, 1000);

    }, 1000);
    const squares = document.querySelectorAll(".loader div");

const path = [0, 1, 2, 5, 8, 7, 6, 3];
let position = 0;

setInterval(() => {
    squares.forEach(square => square.classList.remove("active"));

    for (let i = 0; i < 4; i++) {
        squares[path[(position - i + path.length) % path.length]]
            .classList.add("active");
    }

    position = (position + 1) % path.length;
}, 200);
});