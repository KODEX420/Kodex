window.addEventListener("scroll", () => {
    const opacity = Math.max(0, 0.75 - window.scrollY / 1000);

    document.body.style.backgroundImage = `
        linear-gradient(
            rgba(40,1,55,${opacity}),
            rgba(64,1,1,${opacity}),
            rgba(112,44,12,${opacity})
        ),
        url("fuckno.jpeg")
    `;
});