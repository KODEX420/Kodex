document.addEventListener("DOMContentLoaded", () => {

    // POPUP
    const button = document.getElementById("enterBtn");
    const popup = document.getElementById("Popup");
    const closeBtn = document.getElementById("closeBtn");
    const voidEnterBtn = document.getElementById("voidEnterBtn");

    button.addEventListener("click", () => {
        popup.style.display = "flex";
    });

    closeBtn.addEventListener("click", () => {
        popup.style.display = "none";
    });

    voidEnterBtn.addEventListener("click", () => {
        popup.style.display = "none";
    });


    // GLITCH TEXT
    const corrupt = [
        "█", "▓", "▒", "░",
        "0", "1", "X", "#",
        "@", "%", "&", "?",
        "Ø", "Ξ", "ᄂ", "Δ"
    ];

    function glitchText(element) {
        const original = element.textContent;

        setInterval(() => {
            let text = original.split("");
            const amount = Math.floor(Math.random() * 3) + 1;

            for (let i = 0; i < amount; i++) {
                const index = Math.floor(Math.random() * text.length);

                if (text[index] !== " ") {
                    text[index] =
                        corrupt[Math.floor(Math.random() * corrupt.length)];
                }
            }

            element.textContent = text.join("");

            setTimeout(() => {
                element.textContent = original;
            }, 100);

        }, Math.random() * 1500 + 500);
    }

    glitchText(document.querySelector("h1"));
    glitchText(document.querySelector("h2"));
    glitchText(document.querySelector("h3"));

});