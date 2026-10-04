document.addEventListener("DOMContentLoaded", () => {

    const cover = document.getElementById("cover");
    const title = document.getElementById("title");
    const year = document.getElementById("year");
    const songs = document.getElementById("songs");
    const next = document.getElementById("next");
    const prev = document.getElementById("prev");

    let albums = [];
    let currentAlbum = 0;

    async function loadAlbums() {
        try {
            const response = await fetch("./albums.json");

            if (!response.ok)
                throw new Error(`albums.json: ${response.status}`);

            albums = await response.json();

            console.log("ALBUMS LOADED:", albums);

            showAlbum();

        } catch (error) {
            console.error("FAILED:", error);
            title.textContent = "ALBUMS FAILED TO LOAD";
        }
    }

    function showAlbum() {

        if (!albums.length) return;

        const album = albums[currentAlbum];

        console.log("SHOWING:", album);

        cover.src = `./${album.cover}`;
        cover.alt = album.title;

        title.textContent = album.title;
        year.textContent = album.year;

        songs.innerHTML = "";

        album.songs.forEach((song, index) => {
            const li = document.createElement("li");
            li.textContent =  song;
            songs.appendChild(li);
        });
    }

    next.addEventListener("click", () => {

        if (!albums.length) return;

        currentAlbum = (currentAlbum + 1) % albums.length;

        showAlbum();
    });

    prev.addEventListener("click", () => {

        if (!albums.length) return;

        currentAlbum = (currentAlbum - 1 + albums.length) % albums.length;

        showAlbum();
    });

    loadAlbums();

});