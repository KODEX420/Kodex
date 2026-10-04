import json


albums = [
    {
        "title": "I Want to Die In New Orleans",
        "year": 2018,
        "cover": "Images/I_want_to_die_in_new_orleans.jpg",
        "songs": [
            "King Tulip",
            "Bring out Your Dead",
            "Nicotine Patches",
            "10,000 Degrees",
            "122 Days",
            "Phantom Menace",
            "Krewe Du Vieux (Comedy & Tragedy)",
            "WAR TIME ALL THE TIME",
            "Coma",
            "Long Gone (Save Me from This Hell)",
            "Meet Mr. NICEGUY",
            "Carrollton",
            "Fuck the Industry",
            "I No Longer Fear the Razor Guarding My Heel (IV)"
        ]
    },

    {
        "title": "Stop Staring At the Shadows",
        "year": 2020,
        "cover": "Images/stop_staring_at_the_shadows.jpg",
        "songs": [
            "All Dogs Go to Heaven",
            "I Wanna Be Romanticized",
            "One Last Look at the Damage",
            "[whispers Indistinctly]",
            "Mega Zeph",
            "Putrid Pride",
            "That Just Isn't Empirically Possible",
            "What the Fuck is Happening",
            "Bizarro",
            "Scope Set",
            "Fuck Your Culture",
            "...And to Those I Love, Thanks for Sticking Around"
        ]
    },

    {
        "title": "Long Term Effects of SUFFERING",
        "year": 2021,
        "cover": "Images/long_term_effects_of_suffering.jpg",
        "songs": [
            "Degeneration in the Key of A Minor",
            "If Self-Destruction Was an Olympic Event, I’d Be Tonya Harding",
            "Life Is but a Stream~",
            "5 Grand at 8 to 1",
            "WE ENVY NOTHING IN THE WORLD.",
            "Lighting the Flames of My Own Personal Hell",
            "New Profile Pic",
            "Bleach",
            "Forget It",
            "Avalon",
            "Materialism as a Means to an End",
            "Ugliest",
            "The Number You Have Dialed Is Not in Service"
        ]
    },

    {
        "title": "Sing Me a Lullaby, My Sweet Temptation",
        "year": 2022,
        "cover": "Images/sing_me_a_lullaby_my_sweet_temptation.jpg",
        "songs": [
            "Genesis",
            "Matte Black",
            "Fucking Your Culture",
            "1000 Blunts",
            "In Constant Sorrow",
            "Escape From BABYLON",
            "Ashes of Luxury",
            "Resistance Is Useless",
            "Eulogy",
            "No Matter Which Direction I'm Going In, I Never Chase These Hoes",
            "$uicideboy$ Were Better In 2015",
            "Unlucky Me",
            "THE_EVIL_THAT_MEN_DO"
        ]
    },

    {
        "title": "New World Depression",
        "year": 2024,
        "cover": "Images/new_world_depression.jpg",
        "songs": [
            "Lone Wolf Hysteria",
            "Mental Clarity Is a Luxury I Can't Afford",
            "The Thin Grey Line",
            "Thorns",
            "Misery in Waking Hours",
            "Burgundy",
            "Transgressions",
            "Are You Going to See the Rose in the Vase, or the Dust on the Table",
            "All of My Problems Always Involve Me",
            "The Light at the End of the Tunnel for $9.99 a Month",
            "Drag 'Em to the River (Totalitarian Remix)",
            "Us Vs. Them",
            "Kill Yourself V"
        ]
    },

    {
        "title": "THY KINGDOM COME",
        "year": 2025,
        "cover": "Images/thy_kingdom_come.jpg",
        "songs": [
            "COUNT YOUR BLESSINGS",
            "Napoleon",
            "Oh, What a Wretched Man I Am!",
            "Full of Grace (I Refuse to Tend My Own Grave)",
            "Chain Breaker",
            "Now and at the Hour of Our Death (feat. BONES)",
            "Self-Inflicted",
            "GREY+GREY+GREY",
            "Carried Away",
            "Monochromatic"
        ]
    },

    {
        "title": "THY WILL BE DONE",
        "year": 2025,
        "cover": "Images/thy_will_be_done.jpg",
        "songs": [
            "Leviticus",
            "2009 Reggie Bush",
            "BLOODSWEAT",
            "Angel Grove",
            "Whatever Floats Your Boat Will Definitely Sink My Ship",
            "MSY",
            "Old Addicts, New Habits",
            "Frenzy",
            "Hypernormalisation",
            "Fuck Ups"
        ]
    }
]


with open("albums.json", "w", encoding="utf-8") as file:
    json.dump(albums, file, indent=4, ensure_ascii=False)


print("albums.json created successfully.")
print(f"{len(albums)} albums added.")