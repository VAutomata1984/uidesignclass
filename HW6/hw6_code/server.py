from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

""" 
UI HW 6 - Search Application Functionality
Author: Matthew Vollo
Started: 06/23/2026
Finished: 06/26/2026
"""

# DATA 
games = { 
    "1": {
        "id": 1,
        "title": "Silent Hill",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/5d/SH1_rifle.jpg",
        "year": "1999",
        "summary": "Silent Hill is a 1999 survival horror video game developed by Konami's Team Silent and published by Konami for the PlayStation. It is the first installment in the Silent Hill video game series. The game follows Harry Mason as he searches for his missing adopted daughter in the eponymous fictional American town of Silent Hill. Stumbling upon a cult conducting a rite to revive a deity it worships, he discovers her true origin.",
        "dev":"Team Silent",
        "pub":"Konami",
        "platforms":"PS1",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers",
        "similar":["2","3","4","5"]
    },
    "2":{
        "id": 2,
        "title": "Silent Hill 2",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0lXSKrtpLOIe0ZIhpXuJ0pISSJNNhLWeBSR2Pf6dZeQ&s=10",
        "year": "2001",
        "summary": "Silent Hill 2 is a 2001 survival horror video game developed by Konami's Team Silent and published by Konami for the PlayStation 2. The second installment in the Silent Hill series, Silent Hill 2 centers on James Sunderland, a widower who journeys to the town of Silent Hill after receiving a letter from his dead wife. ",
        "dev":"Team Silent",
        "pub":"Konami",
        "platforms":"PS2, Xbox, Windows",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers",
        "similar":["1","3","4","5"]
    },
    "3":{
        "id": 3,
        "title": "Silent Hill 3",
        "image": "https://i.ytimg.com/vi/r2NLWqFeifw/sddefault.jpg",
        "year": "2003",
        "summary": "Silent Hill 3 is a 2003 survival horror video game developed by Konami's Team Silent and published by Konami for the PlayStation 2. The third installment in the Silent Hill series and a direct sequel to the first Silent Hill game follows Heather Mason, a teenager who becomes entangled in the machinations of the town's cult, which seeks to revive a malevolent deity.",
        "dev":"Team Silent",
        "pub":"Konami",
        "platforms":"PS2, Windows",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers",
        "similar":["1","2","4","5"]
    },
    "4":{
        "id": 4,
        "title": "Silent Hill 4",
        "image": "https://i0.wp.com/bloody-disgusting.com/wp-content/uploads/2020/07/Desktop-Screenshot-2019.05.18-14.07.29.17.jpg?resize=1000%2C600&ssl=1",
        "year": "2004",
        "summary": "Unlike the previous installments, which were set primarily in the town of Silent Hill, this game is set in the southern part of the fictional city of Ashfield, and follows Henry Townshend as he attempts to escape from his locked-down apartment. During the course of the game, Henry explores a series of supernatural worlds and finds himself in conflict with an undead serial killer named Walter Sullivan.",
        "dev":"Team Silent",
        "pub":"Konami",
        "platforms":"PS2, Xbox, Windows",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "GOG, Secondhand Sellers",
        "similar":["1","2","3","5"]
    },
    "5":{
        "id": 5,
        "title": "Silent Hill: Shattered Memories",
        "image": "https://www.hardcoregaming101.net/wp-content/uploads/2021/10/shattered-memories-28.jpg",
        "year": "2009",
        "summary": "Shattered Memories is a reimagination of the first game and retains the premise—Harry Mason's quest to find his missing daughter in the fictitious American town of Silent Hill—but is set in a different fictional universe and has a different plot, and altered characters, alongside new ones. ",
        "dev":"Climax Studios",
        "pub":"Konami",
        "platforms":"Wii, PS2, PSP",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers",
        "similar":["1", "14"]
    },
    "6":{
        "id": 6,
        "title": "Resident Evil Requiem",
        "image": "https://www.gamereactor.eu/media/12/residentevilrequiem_4641263b.jpg",
        "year": "2026",
        "summary": "It is the ninth main game in the Resident Evil series, following Resident Evil Village (2021). It features a new playable character, the FBI analyst Grace Ashcroft, who investigates a series of mysterious deaths involving the survivors of the Raccoon City incident with the aid of the federal agent Leon S. Kennedy.",
        "dev":"Capcom",
        "pub":"Capcom",
        "platforms":"Nintendo Switch 2, PS5, Windows, Xbox Series X/S",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Steam, Playstation Online Store, Xbox Online Store, Physical Stores",
        "similar":["2", "7", "8", "14"]
    },
    "7":{
        "id": 7,
        "title": "Resident Evil - Code Veronica",
        "image": "https://www.oldgamehermit.com/wp-content/uploads/2020/04/codev2.png",
        "year": "2000",
        "summary": "The story takes place three months after the events of Resident Evil 2 (1998) and the concurrent destruction of Raccoon City as seen in Resident Evil 3: Nemesis (1999). It follows Claire Redfield and her brother Chris Redfield in their efforts to survive a viral outbreak at a remote prison island in the Southern Ocean and a research facility in Antarctica.",
        "dev":"Capcom Production Studio 4",
        "pub":"Capcom",
        "platforms":"Dreamcast, PS2, Gamecube, Playstation 3, Xbox 360",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Playstation Online Store",
        "similar":["1", "2", "8"]

    },
    "8":{
        "id": 8,
        "title": "Resident Evil 3 - Nemesis",
        "image": "https://www.oldgamehermit.com/wp-content/uploads/2017/10/re3-3.jpg",
        "year": "1999",
        "summary": "The player must control former elite agent Jill Valentine as she escapes from Raccoon City, which has been overrun by zombies. Choices through the game affect how the story unfolds and which ending is achieved.",
        "dev":"Capcom",
        "pub":"Capcom",
        "platforms":"Playstation, Windows, Dreamcast, Gamecube",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "GOG, Secondhand Sellers",
        "similar":["1", "2", "7"]
    },
    "9":{
        "id": 9,
        "title": "Lost in Vivo",
        "image": "https://storage.ghost.io/c/c0/e7/c0e78dd7-e7af-4603-8ab9-09f05cab06f3/content/images/size/w2000/2022/04/3fb4351b9078014bda5c4f3b9a2286d15f6d2bcdr1-2048-1152v2_uhq-3.jpg",
        "year": "2018",
        "summary": "Heavily inspired by Silent Hill, it follows a patient undergoing Vivo exposure therapy who bravely chases their service dog down a flooded sewer drain, only to descend into a terrifying, claustrophobic nightmare rooted in their own psyche.",
        "dev":"KIRA",
        "pub":"KIRA",
        "platforms":"Windows",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Steam",
        "similar":["1", "2", "3", "8"]
    },
    "10":{
        "id": 10,
        "title": "Haunting Ground",
        "image": "https://www.hardcoregaming101.net/wp-content/uploads/2017/12/hauntingground-15-e1513613450969.png",
        "year": "2005",
        "summary": "The story follows Fiona Belli, a young woman who wakes up in the dungeon of a castle after being involved in a car accident. The player controls Fiona as she befriends a White Shepherd, Hewie, and explores the castle with his aid to seek a means of escape and unravel the mysteries of it and its inhabitants.",
        "dev":"Capcom",
        "pub":"Capcom",
        "platforms":"PS2",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers... good luck finding a copy of this one for cheap.",
        "similar":["3", "11"]
    },
    "11":{
        "id": 11,
        "title": "Rule of Rose",
        "image": "https://gaming-cdn.com/images/news/articles/17611/cover/1000x563/bloober-team-says-its-announcement-does-not-concern-rule-of-rose-cover69812a0261299.jpg",
        "year": "2006",
        "summary": "Set in Britain in 1930, the plot revolves around a nineteen-year-old woman named Jennifer, who finds herself trapped in a world dominated by young girls who have formed a social hierarchy known as the Red Crayon Aristocrats.",
        "dev":"Punchline",
        "pub":"Atlus USA",
        "platforms":"PS2",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers... good luck finding a copy of this one for cheap.",
        "similar":["3", "10"]
    },
    "12":{
        "id": 12,
        "title": "Koudelka",
        "image": "https://storage.ghost.io/c/c0/e7/c0e78dd7-e7af-4603-8ab9-09f05cab06f3/content/images/2023/05/MV5BMTczYzA4YTItNzE0MC00ODViLTg3MTQtNDg4MzcyOGEyMGYzXkEyXkFqcGdeQXVyMTEwNDU1MzEy._V1_.jpg",
        "year": "2000",
        "summary": "Set in the haunted Nemeton Monastery in Wales, the plot follows protagonists Koudelka Iasant, Edward Plunkett and Bishop James O'Flaherty as they uncover Nemeton's secrets and confront monsters created from its dark past.",
        "dev":"Sacnoth",
        "pub":"SNK",
        "platforms":"Playstation",
        "genre":"Role-playing",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers",
        "similar":["1", "13"]
    },
    "13":{
        "id": 13,
        "title": "Parasite Eve",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjUAkedndmJ2sQ-3IcVIpaJUhm1d_VSRzXsg&s",
        "year": "1998",
        "summary": "The game is a sequel to the novel Parasite Eve, written by Hideaki Sena; it is the first game in the Parasite Eve video game series. The story follows New York City police officer Aya Brea over a six-day span in 1997 as she attempts to stop the Eve, a woman who plans to destroy the human race through spontaneous human combustion. Players explore levels set in areas of New York while utilizing a pausable real-time combat system along with several role-playing elements.",
        "dev":"Square",
        "pub":"Square Electronic Arts",
        "platforms":"Playstation",
        "genre":"Role-playing",
        "mode":"Single-Player",
        "w2b": "Secondhand Sellers",
        "similar":["1", "12"]
    },
    "14":{
        "id": 14,
        "title": "Slender: The Arrival",
        "image": "https://assets.nintendo.com/image/upload/ar_16:9,b_auto:border,c_lpad/b_white/f_auto/q_auto/dpr_1.5/store/software/switch/70010000016226/d795043a7106755ef117255185b56839da5bef08965e803a507a1a34a6bc247e",
        "year": "2013",
        "summary": "The game revolves around a young woman who ventures into the woods to investigate the disappearance of her childhood best friend. Equipped only with a flashlight, the player explores abandoned locations and completes objectives while avoiding the Slender Man and his proxies.",
        "dev":"Blue Isle Studios",
        "pub":"Blue Isle Studios",
        "platforms":"OS X, Windows, PlayStation 3, Xbox 360, PlayStation 4, Xbox One, Wii U, Nintendo Switch, Android, iOS",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Steam, Playstation Store, Nintendo Store, Xbox Store",
        "similar":["5", "15"]
    },
    "15":{
        "id": 15,
        "title": "Routine",
        "image": "https://cdn.mos.cms.futurecdn.net/6GHWApDcqF2zkZpbC2Gxyj.png",
        "year": "2025",
        "summary": "Set on a lunar base, the story follows an unnamed protagonist unraveling a mysterious incident that led to the base's decline. The game is played from a first-person perspective, with the player exploring the base and using a special device to fight hostile robots, interact with the environment, and perform other actions.",
        "dev":"Lunar Software",
        "pub":"Raw Fury",
        "platforms":"Windows, Xbox One, Xbox Series X/S",
        "genre":"Survival Horror",
        "mode":"Single-Player",
        "w2b": "Steam, Xbox Store",
        "similar":["14"]
    }
}

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def boo_world():
   return render_template('homepage.html',games=games)   

@app.route("/search", methods=['GET', 'POST'])
def search():
   search_text = request.form.get('search_text', '').strip()
   if not search_text:
        return render_template('homepage.html', games=games)  # or redirect back
   
   results = [game for game in games.values() if search_text in game['title']]

   return render_template('search_results.html', results=results, search_text=search_text, games=games)

@app.route("/view/<id>", methods=['GET'])
def view(id):
    game = games.get(id)
    return render_template('view.html', games=games, id=id)


if __name__ == '__main__':
   app.run(debug = True)

