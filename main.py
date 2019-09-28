from pypercard import Card, CardApp, Inputs
import random


text_size = 32


def name_entry(data, form):
    if form:
        data["name"] = form.strip()
        return "intro1"
    else:
        return "nameerror"

def to_patio(data, form):
    if data["open"]:
        return "patio_open"
    else:
        return "patio_closed"

def to_front_door(data, form):
    if data["open"]:
        return "front_door_open"
    else:
        return "front_door_closed"

def to_back_door(data, form):
    if data["open"]:
        return "back_door_open"
    else:
        return "back_door_closed"

def to_inscription(data, form):
    if data["inscription"]:
        return "inscription2b"
    else:
        data["inscription"] = True
        return "inscription1"

def to_encounter(data, form):
    if data["encounter"]:
        if data["open"]:
            return "forest_path"
        else:
            return "interview"
    else:
        data["encounter"] = True
        return "encounter1"


def to_answer(data, form):
    wrong = ["interview_no1", "interview_no2", "interview_no3", "interview_no4", "interview_no5"]
    if form:
        answer = form.lower().strip()
        if answer == "telesphoros":
            data["open"] = True
            return "interview_end"
        else:
            return random.choice(wrong)
    else:
        return random.choice(wrong)


def to_red_book(data, form):
    if data["red_book"]:
        if data["locked"]:
            return "book_lock"
        else:
            return "red_book"
    else:
        data["red_book"] = True
        return "unlock1"

def to_unlock(data, form):
    data["message"] = "You must enter a four digit number."
    if form:
        try:
            code = int(form.strip())
            if code < 10000 and code >=0:
                if code == 1943:
                    data["locked"] = False
                    return "red1"
                else:
                    data["message"] = "Wrong combination, try again."
            else:
                data["message"] = "The number should be between 0000 and 9999."
        except Exception:
            data["message"] = "Please enter four valid digits."
    return "locked"


def to_dining_room(data, form):
    if data["instructions"]:
        if data["red_book"]:
            return "finale"
        else:
            return "waiting"
    else:
        data["instructions"] = True
        return "instruct"

cards = [
    Card("hello", text="Hello, please enter your forename...",
        form=Inputs.TEXTBOX, buttons=[{"label": "OK", "target": name_entry},]),
    Card("nameerror", text="Please enter your name.", auto_advance=3,
        auto_target="hello"),
    Card("intro1", text_size=text_size, text="Hello, {name}.\n\nPlease ensure you have sound turned on, or headphones plugged in. Use buttons and forms to proceed through the game.\n\nIf there are no buttons visible, it means the screen will advance after a pre-determined period of time.\n\nCan you solve the riddle of the Alchemist's Tower?",
    buttons=[{"label": "OK", "target": "intro2"}]),
    Card("intro2", sound="music/opening_chords.wav", auto_advance=2, auto_target="intro2b"),
    Card("intro2b", text="[size=48]The Alchemist's Tower\n\n[/size][size=32]A mystery set on the banks of Lake Zurich.\n\n[/size][size=18]by Nicholas H.Tollervey[/size]", auto_advance=6, auto_target="intro2c"),
    Card("intro2c", auto_advance=2, auto_target="intro3"),
    Card("intro3", text_size=text_size, text="Lake Zurich reflected the whispy white autumn clouds, yet the water was clear enough that it was easy to spot fish and see the sandy bed several metres below. The fresh smell of reeds and algae was in the air. Distant and indistinct sounds from the shore could be heard over the lapping of the water against the hull.\n\nThe dinghy glided through the water towards an outcrop covered in trees within which could be seen an irregular group of white-washed towers and walls.\n\nThe taciturn youth at the helm had simply promised to land at a secret location ripe for exploration.", auto_advance=32, auto_target="landing"),
    Card("landing", background="img/from_lake.png", auto_advance=10.5, auto_target="landed"),
    Card("landed", text_size=text_size, text='"{name}, this is where you get off", said the youth.\n\nHe avoided making eye contact whilst offering a hand onto the shore of the lake.\n\nAs quickly as possible he pushed off and, without turning around, waved as he sailed towards the middle of the lake.', sound="sfx/lake.wav", sound_repeat=True, buttons=[{"label": "OK", "target": to_patio}]),
    Card("patio_closed", background="img/patio_closed.png", buttons=[
        {"label": "◀", "target": "beach"},
        {"label": "▲", "target": to_front_door},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("patio_open", background="img/patio_open.png", buttons=[
        {"label": "◀", "target": "beach"},
        {"label": "▲", "target": to_front_door},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("beach", background="img/beach.png", buttons=[
        {"label": "◀", "target": "lakeside"},
        {"label": "▲", "target": "undergrowth"},
        {"label": "▶", "target": to_patio},
    ], sound="sfx/lake.wav", sound_repeat=True),
    Card("lakeside", background="img/lakeside.png", buttons=[
        {"label": "▶", "target": "beach"},
    ], sound="sfx/lake.wav", sound_repeat=True),
    Card("front_door_open", background="img/front_door_open.png", buttons=[
        {"label": "◀", "target": "undergrowth"},
        {"label": "Stone", "target": "stone"},
        {"label": "▲", "target": "front_courtyard"},
        {"label": "▶", "target": "lake_reeds"},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("front_door_closed", background="img/front_door_closed.png", buttons=[
        {"label": "◀", "target": "undergrowth"},
        {"label": "Stone", "target": "stone"},
        {"label": "▶", "target": "lake_reeds"},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("back_door_open", background="img/back_door_open.png", buttons=[
        {"label": "▲", "target": "back_courtyard"},
        {"label": "▼", "target": "back_garden"},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("back_door_closed", background="img/back_door_closed.png", buttons=[
        {"label": "▼", "target": "back_garden"},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("stone", background="img/stone.png", buttons=[
        {"label": "Read", "target": to_inscription},
        {"label": "▼", "target": to_front_door},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("inscription1", text_size=text_size, text="Set on a pedestal under the tree was a weathered and roughly carved stone. The inscriptions appeared to be in Greek and contained mysterious looking magical symbols.\n\nIn the centre was a small figure (named as Telesphoros) wearing a hooded cloak and carrying a lantern, greeting visitors or perhaps beckoning to them with a wave of his hand.",
    sound="music/solo_violin.wav", auto_advance=20,
    auto_target="inscription2a"),
    Card("inscription2a", background="img/inscription.png", auto_advance=24,
        auto_target="inscription3"),
    Card("inscription2b", background="img/inscription.png", buttons=[
        {"label": "OK", "target": "stone"},
        {"label": "Re-translate", "target": "inscription4b"},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("inscription3", text_size=text_size, text="The circular shape of the carving looked like the pupil of an eye, keeping watch over visitors and looking into their souls.\n\nApparently the Greek inscriptions were once translated into English, and it was said that they didn't seem to make much sense.\n\nThey were a sort of incantation or dedication written by the alchemist who had once lived in the tower.", auto_advance=20,
        auto_target="inscription4a"),
    Card("inscription4a", text_size=text_size, text="Time is a child playing, like a child playing a board game, the kingdom of the child.\n\nThis is Telesphoros, who roams through the dark regions of this cosmos and glows like a star out of the depths.\n\nHe points the way to the gates of the sun and to the land of dreams.", auto_advance=20,
        auto_target="stone"),
    Card("inscription4b", text_size=text_size, text="Time is a child playing, like a child playing a board game, the kingdom of the child.\n\nThis is Telesphoros, who roams through the dark regions of this cosmos and glows like a star out of the depths.\n\nHe points the way to the gates of the sun and to the land of dreams.",
        buttons=[{"label": "OK", "target": "stone"},]),
    Card("undergrowth", background="img/undergrowth.png", buttons=[
        {"label": "◀", "target": "walls"},
        {"label": "▲", "target": to_front_door},
        {"label": "▶", "target": "beach"},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("lake_reeds", background="img/lake_reeds.png", buttons=[
        {"label": "◀", "target": to_front_door},
        {"label": "▲", "target": "reed_wall"},
    ], sound="sfx/lake.wav", sound_repeat=True),
    Card("reed_wall", background="img/reed_wall.png", buttons=[
        {"label": "▲", "target": "lake_reeds"},
        {"label": "▶", "target": "back_garden"},
    ], sound="sfx/lake.wav", sound_repeat=True),
    Card("back_garden", background="img/back_garden.png", buttons=[
        {"label": "◀", "target": "reed_wall"},
        {"label": "▲", "target": to_back_door},
        {"label": "▶", "target": "back_woods"},
    ], sound="sfx/nature.wav", sound_repeat=True),
    Card("walls", background="img/walls.png", buttons=[
        {"label": "◀", "target": "rear_tower"},
        {"label": "▶", "target": "undergrowth"},
    ], sound="sfx/woods.wav", sound_repeat=True),
    Card("rear_tower", background="img/rear_tower.png", buttons=[
        {"label": "◀", "target": "back_woods"},
        {"label": "▶", "target": "walls"},
    ], sound="sfx/woods.wav", sound_repeat=True),
    Card("back_woods", background="img/back_woods.png", buttons=[
        {"label": "◀", "target": "woods"},
        {"label": "▲", "target": "back_garden"},
        {"label": "▶", "target": "rear_tower"},
    ], sound="sfx/woods.wav", sound_repeat=True),
    Card("woods", background="img/woods.png", buttons=[
        {"label": "◀", "target": to_encounter},
        {"label": "▶", "target": "back_woods"},
    ], sound="sfx/woods.wav", sound_repeat=True),
    Card("forest_path", background="img/forest_path.png", buttons=[
        {"label": "▲", "target": "woods"},
    ], sound="sfx/woods.wav", sound_repeat=True),
    Card("encounter1", background="img/jung2.png", auto_advance=4,
    auto_target="encounter2",
    sound="music/chords_and_stopping.wav"),
    Card("encounter2", text_size=text_size, text="From behind a tree emerged a spry looking elderly man.\n\nHis clothing was of Victorian cut and he wore wire rimmed glasses that gave him the air of an intellectual. His hair was grey and he sported a well groomed moustache.\n\nBut it was his piercing eyes that grabbed one's attention.\n\n  \"My name is Carl Gustav\", he said with a thick Swiss accent.\n\n  \"What are you doing in my land?\"",
    auto_advance=18, auto_target="encounter3"),
    Card("encounter3", background="img/jung_close.png", auto_advance=2,
    auto_target="encounter4"),
    Card("encounter4", text_size=text_size, text="  \"Sir, I do not wish to intrude\", you replied.\n\nHe took the measure of you as his eyes twinkled from behind his glasses.\n\n  \"Hmmmm. I don't usually get visitors, so I may yet be glad of your company.\"\n\n  You told him that you'd heard that this, \"was a place of exploration.\"\n\n  \"That it is, but not in the way I think you mean. I wonder if you have explored much yet?\", was his reply.",
    auto_advance=18, auto_target="encounter5"),
    Card("encounter5", text_size=text_size, text="He continued, \"If you can answer me a question, I'll open the tower for you.\"\n\nThis was an offer too good to miss. The tower felt like it was alive and asking to be explored.\n\n  \"I assume you've seen the stone standing guard by the front door? If you can tell me the name of the character carved therein, I'll let you in the tower.\"",
    auto_advance=16, auto_target="interview"),

    Card("interview", text_size=text_size, text="Carl Gustav looked you in the eye and asked, \"What is the name on the guarding stone?\" (Type your answer below.)", form=Inputs.TEXTBOX, buttons=[
        {"label": "Answer", "target": to_answer},
        {"label": "▼", "target": "woods"},
    ], sound="sfx/woods.wav", sound_repeat=True),
    Card("interview_end", text_size=text_size, text="The old man broke into a smile.\n\n\"Correct!\", he exclaimed.\n\nWith that, he stood up and walked through the woods in the direction of the tower.", sound="sfx/gravel_steps.wav",
    auto_advance=10, auto_target="woods"),
    Card("interview_no1", text_size=text_size, text="The old man shook his head and said, \"Try again, friend\".",
    auto_advance=4, auto_target="interview"),
    Card("interview_no2", text_size=text_size, text="\"That's not it\", said Carl Gustav.",
    auto_advance=4, auto_target="interview"),
    Card("interview_no3", text_size=text_size, text="Carl Gustav smiled, shook his head and said, \"I'm afraid that's incorrect\".",
    auto_advance=4, auto_target="interview"),
    Card("interview_no4", text_size=text_size, text="\"Wrong, better luck next time...\", said the old man.",
    auto_advance=4, auto_target="interview"),
    Card("interview_no5", text_size=text_size, text="\"No my friend, perhaps go take a look?\", said the old man.",
    auto_advance=4, auto_target="interview"),
    Card("front_courtyard", background="img/front_door_out.png",
        sound="sfx/nature.wav", sound_repeat=True, buttons=[
            {"label": "▲", "target": to_front_door},
            {"label": "▼", "target": "back_courtyard"},
            {"label": "▶", "target": "small_tower_door"},
        ]),
    Card("back_courtyard", background="img/arches.png",
        sound="sfx/fireplace.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "courtyard_towers"},
            {"label": "▲", "target": "under_arch"},
            {"label": "▼", "target": "front_courtyard"},
            
        ]),
    Card("courtyard_towers", background="img/courtyard_towers.png",
         sound="sfx/nature.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "large_tower_door"},
            {"label": "▶", "target": "back_courtyard"},
         ]),
    Card("large_tower_door", background="img/courtyard_tower_door.png",
         sound="sfx/nature.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "courtyard_tower_round"},
            {"label": "▲", "target": to_dining_room},
            {"label": "▶", "target": "courtyard_towers"},
         ]),
    Card("courtyard_tower_round", background="img/courtyard_tower_round.png",
         sound="sfx/nature.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "small_tower_door"},
            {"label": "▶", "target": "large_tower_door"},
         ]),
    Card("small_tower_door", background="img/tower_door.png",
         sound="sfx/nature.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "front_courtyard"},
            {"label": "▲", "target": "stairs"},
            {"label": "▶", "target": "courtyard_tower_round"},
         ]),
    Card("stairs", background="img/fireplace.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "basin"},
            {"label": "Up", "target": "window_view"},
            {"label": "▲", "target": "small_tower_door"},
            {"label": "▶", "target": "hearth"},
         ]),
    Card("hearth", background="img/hearth.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "stairs"},
            {"label": "▶", "target": "basin"},
         ]),
    Card("basin", background="img/basin.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "hearth"},
            {"label": "▶", "target": "stairs"},
         ]),
    Card("dining_room", background="img/dining_room.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "▼", "target": "large_tower_door"},
         ]),
    Card("under_arch", background="img/under_arch.png",
         sound="sfx/fireplace.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "wood_store"},
            {"label": "▼", "target": "back_courtyard"},
            {"label": "▶", "target": "window_reeds"},
         ]),
    Card("wood_store", background="img/wood_store.png",
         sound="sfx/fireplace.wav", sound_repeat=True, buttons=[
            {"label": "▼", "target": "under_arch"},
         ]),
    Card("window_reeds", background="img/window_reeds.png",
         sound="sfx/lake.wav", sound_repeat=True, buttons=[
            {"label": "▼", "target": "under_arch"},
         ]),
    Card("window_view", background="img/window_view.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "Down", "target": "stairs"},
            {"label": "▲", "target": "view_down_courtyard"},
            {"label": "▶", "target": to_red_book},
         ]),
    Card("view_down_courtyard", background="img/view_down_courtyard.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "▼", "target": "window_view"},
         ]),
    Card("red_book", background="img/red_book.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "window_view"},
            {"label": "Read", "target": "book1"},
         ]),
    Card("book1", 
         text_size=text_size,
         text="There was a page with an image of a winged old man stood between two trees with a Python at his feet.\n\nThe text explained, \"I am Philemon, and I am conduit for the multitude within you. Be still, and speak with me of your explorations within yourself. Give me voice that I may tell you of our internal reservoir of collective knowledge. Then know yourself, and allow the multitude to enlarge your Self.\"",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "red_book"},
            {"label": "▶", "target": "book2"},
         ]),
    Card("book2", background="img/book1.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "book1"},
            {"label": "▶", "target": "book3"},
         ]),
    Card("book3", 
         text_size=text_size,
         text="Another page contained a picture of a serpent circling a glowing orb.\n\nWords explained, \"Knowing and using the power of the serpent means you create new colourful magic and alchemy. It allows you to harness the external reservoir of collective knowledge.\"",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "book2"},
            {"label": "▶", "target": "book4"},
         ]),
    Card("book4", background="img/book2.png",
         sound="sfx/ticking.wav", sound_repeat=True, buttons=[
            {"label": "◀", "target": "book3"},
            {"label": "▶", "target": "red_book"},
         ]),
    Card("unlock1",
         text_size=48,
         text="The Red Book",
         auto_advance=4,
         auto_target="unlock2",
         sound="sfx/bells.wav"),
    Card("unlock2",
         background="img/red_book.png",
         auto_advance=5,
         auto_target="unlock3"),
    Card("unlock3",
         text_size=text_size,
         text="The Red Book sat on a cluttered desk next to a photograph of the guarding stone and a notepad.\n\nIt was impossible to open the book because of a latch attached to a four digit combination lock binding the covers together.\n\nOn the pad was written a riddle, \"Sink your efforts into the year of the bowl\".",
         auto_advance=20,
         auto_target="book_lock"),
    Card("book_lock",
        text_size=text_size,
        text="Enter the four digit code to unlock the book:",
        form=Inputs.TEXTBOX, buttons=[
            {"label": "Unlock", "target": to_unlock},
            {"label": "▼", "target": "window_view"},
        ], sound="sfx/ticking.wav", sound_repeat=True),
    Card("locked",
         text_size=text_size,
         text="{message}",
         auto_advance=3,
         auto_target="book_lock"),
    Card("red1", 
         text_size=text_size,
         text="The latch came loose and the lock fell onto the desk with a gentle thud.\n\nUpon opening the leather bound covers a whiff of tobacco smoke was detected, as if the author or reader was a regular pipe smoker. On the front page was written in large Gothic script, \"Liber Novus\".\n\nWithin the book was page after page of beautifully illuminated prose sitting alongside colourful images of mythical beasts, far off places and strange beings.",
         auto_advance=30,
         auto_target="red2",
         sound="music/violin_and_chords.wav",
         sound_repeat=True),
    Card("red2", 
         background="img/book1.png",
         auto_advance=15,
         auto_target="red3"),
    Card("red3", 
         text_size=text_size,
         text="There was a page with an image of a winged old man stood between two trees with a Python at his feet.\n\nThe text explained, \"I am Philemon, and I am conduit for the multitude within you. Be still, and speak with me of your explorations within yourself. Give me voice that I may tell you of our internal reservoir of collective knowledge. Then know yourself, and allow the multitude to enlarge your Self.\"",
         auto_advance=25,
         auto_target="red4"),
    Card("red4", 
         background="img/book2.png",
         auto_advance=20,
         sound="music/violin_and_chords.wav",
         auto_target="red5"),
    Card("red5", 
         text_size=text_size,
         text="Another page contained a picture of a serpent circling a glowing orb.\n\nWords explained, \"Knowing and using the power of the serpent means you create new colourful magic and alchemy. It allows you to harness the external reservoir of collective knowledge.\"",
         auto_advance=24,
         auto_target="red_book"),
    Card("instruct",
         background="img/dining_room.png",
         auto_advance=5,
         auto_target="instruct2",
         sound="music/chords_and_arpeggios.wav"),
    Card("instruct2",
         background="img/jung.png",
         auto_advance=9,
         auto_target="instruct3"),
    Card("instruct3",
         text_size=text_size,
         text="Carl Gustav pensively sat in a corner of the dining room.\n\nHe hadn't noticed the intrusion and was mumbling to himself.\n\n\"The book must be read, the book is read, only if your have read the book can the transmogrification be explained.\"",
         auto_advance=14,
         auto_target="instruct4"),
    Card("instruct4",
         background="img/jung3.png",
         auto_advance=3,
         auto_target="instruct5"),
    Card("instruct5",
         text_size=text_size,
         text="Suddenly he looked up...\n\nSimiling, he pronounced with great emphasis, \"You must read the read book\".\n\n  \"The book..?\", you asked.\n\nShrugging he simply said, \"The Red Book\".",
         auto_advance=15,
         auto_target="dining_room"),
    Card("waiting",
         background="img/dining_room.png",
         auto_advance=4,
         auto_target="waiting2",
         sound="sfx/bells.wav"),
    Card("waiting2",
         background="img/jung.png",
         auto_advance=5,
         auto_target="waiting3"),
    Card("waiting3",
         text_size=text_size,
         text="Carl Gustav looked up expectantly, searching your face for recognition and then sighed.\n\n\"Read the Red Book\", was all he would say.",
         auto_advance=12,
         auto_target="dining_room"),
    Card("finale",
         background="img/dining_room.png",
         auto_advance=9,
         auto_target="finale2",
         sound="music/chords_and_harmonics.wav"),
    Card("finale2",
         background="img/jung.png",
         auto_advance=9,
         auto_target="finale3"),
    Card("finale3",
         text_size=text_size,
         text="Carl Gustav looked up expectantly, searching your face for recognition and then beamed a huge smile.",
         auto_advance=8,
         auto_target="finale4"),
    Card("finale4",
         background="img/jung3.png",
         auto_advance=3,
         auto_target="finale5"),
    Card("finale5",
         text_size=text_size,
         text="\"{name}, my child. You are ready to hear the alchemist's secret.\"",
         auto_advance=5,
         auto_target="finale5b"),
    Card("finale5b",
         text_size=text_size,
         text="\"The alchemy of which I speak involves elements of the psyche. The exploration that happens here, is of the soul.\"",
         auto_advance=8,
         auto_target="finale5c"),
    Card("finale5c",
         text_size=text_size,
         text="\"The transformation you must achieve is within yourself.\"\n\n\"Can you assuage the multitude within you with the multitude of others outside yourself?\"\n\n\"Will you swim in the reservoir with our colourful ancestors..?\"\n\n\"Are you the alchemist of your soul..?\"", 
         auto_advance=14,
         auto_target="finale6"),
    Card("finale6",
         text_size=text_size,
         text="That was when you awoke....",
         auto_advance=4,
         auto_target="finale7"),
    Card("finale7",
         text_size=text_size,
         text="...only to find yourself back on the dinghy.\n\nThe taciturn youth looked at you intently as you passed an outcrop covered in trees within which could be seen an irregular group of white-washed towers and walls.",
         auto_advance=10,
         auto_target="finale8"),
    Card("finale8",
         background="img/bollingen.png",
         auto_advance=5,
         auto_target="finale9"),
    Card("finale9",
         text_size=text_size,
         text="The End.")
]

app = CardApp(stack=cards, name="The Alchemist's Tower",
              font="font/LinLibertine_R.ttf",
              data_store={"open": False, "inscription": False,
              "encounter": False, "locked": True, "red_book": False,
              "instructions": False})
app.run()
