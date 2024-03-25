from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar,messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Downloads\Builded\Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def guess():
    movies = [
    #inside mcu
    'Antman', 'AntManAndTheWasp', 'AntManAndTheWaspQuantumania', 
    'TheAvengers','AvengersAgeOfUltron','AvengersEndgame', 'AvengersInfinityWar', 'AvengersSecretWars', 'AvengersTheKangDynasty',
    'BlackPanther', 'BlackPantherWakandaForever', 
    'BlackWidow', 
    'Blade',
    'CaptainAmericaTheFirstAvenger', 'CaptainAmericaCivilWar','CaptainAmericaBraveNewWorld', 'CaptainAmericaTheWinterSoldier',
    'CaptainMarvel', 'TheMarvels',
    'Deadpool', 'Deadpool2', 'Deadpool&Wolverine',
    'DoctorStrange', 'DoctorStrangeInTheMultiverseOfMadness',
    'Eternals',
    'FantasticFour',
    'GuardiansOfTheGalaxy', 'GuardiansOfTheGalaxyVol2','GuardiansOfTheGalaxyVol3',
    'IronMan', 'IronMan2','IronMan3', 
    'ShangChiAndTheLegendOfTheTenRings', 
    'SpiderMan', 'SpiderMan2','SpiderMan3',
    'SpiderManFarFromHome', 'SpiderManHomecoming','SpiderManNoWayHome',
    'SpiderManIntoTheSpiderVerse','SpuedrManAcrosstheSpiderVerse','SpiderManBeyondtheSpiderVerse',
    'TheAmazingSpiderMan','TheAmazingSpiderMan2',
    'TheIncredibleHulk',
    'Thor', 'ThorLoveAndThunder', 'ThorRagnarok', 'ThorTheDarkWorld',
    'Thunderbolts', 

    #outside mcu
    'Blade1998','Blade2','BladeTrinity'
    'FantasticFour2015'
    'HowardTheDuck',
    'ManThing', 
    'Morbius',
    'PunisherWarZone', 
    'TheNewMutants', 
    'Venom','VenomLetThereBeCarnage','VenomTheLastDance',
    'Logan','XMen', 'XMenApocalypse', 'XMenDaysOfFuturePast', 'XMenOriginsWolverine', 'XMenTheLastStand',

    #marvel series
    'AgentsOfSHIELD', 'AgentCarter', 'Inhumans', 
    'Daredevil','DaredevilBornAgain',
    'JessicaJones', 'LukeCage', 'IronFist', 'TheDefenders',
    'ThePunisher', 'Runaways', 'CloakAndDagger', 'Helstrom',
    'WandaVision', 'TheFalconAndTheWinterSoldier',
    'Loki','LokiSeason2',
    'WhatIf','WhatIfSeason2',
    'Hawkeye', 'MoonKnight', 'MsMarvel', 'SheHulkAttorneyAtLaw',
    'SecretInvasion', 'Ironheart', 'ArmorWars', 'IamGroot',
    'Echo', 'AgathaCovenofChaos', 'SpiderManFreshmanYear','SpiderManSophomoreYear',
    'MarvelZombies', 'XMen97', 'TheGifted', 'Legion'
    ]

    game_list=[]

    length=int(entry_1.get())

    for i in movies:
        if len(i)==length:
            game_list.append(i)

    char=entry_2.get()
    pos=int(entry_3.get())


    for j in game_list:
        if j[pos-1].lower()==char.lower():
            result.set(j)

def check():
    first,second,third=entry_1.get(),entry_2.get(),entry_3.get()
    a="str"
    if first.strip()=="" or second.strip()=="" or third.strip()=="":
        messagebox.showerror("Error","Please fill all the fields")
    else:
        try:
            guess()
        except:
            messagebox.showerror("Error","Please enter valid characters")


window = Tk()

window.geometry("525x370")
window.configure(bg = "#FFFFFF")
window.title("Hangman Guesser")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 370,
    width = 525,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    16,
    46,
    anchor="nw",
    text="Enter the total character in the movie/Series:",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    16,
    109,
    anchor="nw",
    text="Enter the character given:",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    16,
    169,
    anchor="nw",
    text="Enter the position of the given character:",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    58,
    298,
    anchor="nw",
    text="The movie is:",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

result=StringVar()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= check,
    activebackground="#FFFFFF",
    relief="flat"
)
button_1.place(
    x=207,
    y=219,
    width=94.0,
    height=31.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    428.0,
    56.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Roboto",15)
)
entry_1.place(
    x=355.0,
    y=39,
    width=146.0,
    height=33.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    291.0,
    118.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Roboto",15)
)
entry_2.place(
    x=218.0,
    y=101,
    width=146.0,
    height=33.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    397.0,
    177.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Roboto",15)
)
entry_3.place(
    x=324.0,
    y=160,
    width=146.0,
    height=33.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    313.5,
    308.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=result,
    font=("Roboto",15)
)
entry_4.place(
    x=169.0,
    y=291.0,
    width=289.0,
    height=33.0
)
window.resizable(False, False)
window.mainloop()
