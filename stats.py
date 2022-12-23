import datetime
import requests
import json

from os import system
system("title Stats Rinaorc by Krystal#6960")



def clear():
    system("cls")


with open("settings.json", "r") as f:
    config = json.load(f)
header = {"API-Key": config["APIKey"]}
username = input('\n\n\n\n                    [>] Player Name: ')
r = requests.get(url=f"https://api.rinaorc.com/player/{username}", headers=header)
data = r.json()

a = requests.get(url=f"https://api.rinaorc.com/stats/players", headers=header)
serverInfo = a.json()

def menu(data, serverInfo):
    clear()
    
    choice = input(
        "\n                   Choose Info:\n\n        [1] User Info        [2] BedWars Info        \n\n        [3] Clan Info        [4] Change user\n\n                    Choice: ")
    clear()
    if choice == "1":
        
        playerData = data["player"]
        if playerData["isOnline"] == True:
            online = "Online"
        else:
            online = "Offline"
        print(f'''
            : Player Information :
            
        Minecraft UUID: {playerData["uuid"]}
        Rank: {playerData["rank"]["name"]}
        Status: {online}
        Aura: {playerData["aura"]}
        Connection Method: {playerData["connectionMethod"]}

            :       Discord      :
        Discord ID: {playerData["links"]["discord"]}
        Booster: {playerData["hasBoost"]}

            :        Clan        :
        Name: {playerData["clan"]["name"]}
        ID: {playerData["clan"]["id"]}
        TAG: {playerData["clan"]["tag"]}
        Status: {playerData["clan"]["status"]}

        Level: {playerData["clan"]["level"]}
        Experience: {playerData["clan"]["experience"]}''')
        input()
        menu(data, serverInfo)

    if choice == "2":
        
        bedwarsGames = data["player"]["games"]["bedwars"]
        bedwarsStats = data["player"]["stats"]["bedwars"]
        print(f'''
            : Bedwars Statistics :
        
        Username: {data["player"]["name"]}
        Level: {bedwarsGames["level"]}
        Current Win Streak: {bedwarsGames["winStreak"]}
        Best Win Streak: {bedwarsGames["bestWinStreak"]}

            : Solo :
        Break Bed: {bedwarsStats["breakBed"]["total"]["solo"]}
        Games Played: {bedwarsStats["played"]["total"]["solo"]}
        Final Kills: {bedwarsStats["finalKills"]["total"]["solo"]}
        Final Deaths {bedwarsStats["finalDeaths"]["total"]["solo"]}
        Kills: {bedwarsStats["kills"]["total"]["solo"]}
        Bed Lost: {bedwarsStats["lostBed"]["total"]["solo"]}
        Deaths: {bedwarsStats["deaths"]["total"]["solo"]}
        Wins: {bedwarsStats["wins"]["total"]["solo"]}
        Looses: {bedwarsStats["played"]["total"]["solo"]-bedwarsStats["wins"]["total"]["solo"]}

            : Duo :
        Break Bed: {bedwarsStats["breakBed"]["total"]["duo"]}
        Games Played: {bedwarsStats["played"]["total"]["duo"]}
        Final Kills: {bedwarsStats["finalKills"]["total"]["duo"]}
        Final Deaths {bedwarsStats["finalDeaths"]["total"]["duo"]}
        Kills: {bedwarsStats["kills"]["total"]["duo"]}
        Bed Lost: {bedwarsStats["lostBed"]["total"]["duo"]}
        Deaths: {bedwarsStats["deaths"]["total"]["duo"]}
        Wins: {bedwarsStats["wins"]["total"]["duo"]}
        Looses: {bedwarsStats["played"]["total"]["duo"]-bedwarsStats["wins"]["total"]["duo"]}

            : Trio :
        Break Bed: {bedwarsStats["breakBed"]["total"]["trio"]}
        Games Played: {bedwarsStats["played"]["total"]["trio"]}
        Final Kills: {bedwarsStats["finalKills"]["total"]["trio"]}
        Final Deaths {bedwarsStats["finalDeaths"]["total"]["trio"]}
        Kills: {bedwarsStats["kills"]["total"]["trio"]}
        Bed Lost: {bedwarsStats["lostBed"]["total"]["trio"]}
        Deaths: {bedwarsStats["deaths"]["total"]["trio"]}
        Wins: {bedwarsStats["wins"]["total"]["trio"]}
        Looses: {bedwarsStats["played"]["total"]["trio"]-bedwarsStats["wins"]["total"]["trio"]}

            : Quatuor :
        Break Bed: {bedwarsStats["breakBed"]["total"]["quatuor"]}
        Games Played: {bedwarsStats["played"]["total"]["quatuor"]}
        Final Kills: {bedwarsStats["finalKills"]["total"]["quatuor"]}
        Final Deaths {bedwarsStats["finalDeaths"]["total"]["quatuor"]}
        Kills: {bedwarsStats["kills"]["total"]["quatuor"]}
        Bed Lost: {bedwarsStats["lostBed"]["total"]["quatuor"]}
        Deaths: {bedwarsStats["deaths"]["total"]["quatuor"]}
        Wins: {bedwarsStats["wins"]["total"]["quatuor"]}
        Looses: {bedwarsStats["played"]["total"]["quatuor"]-bedwarsStats["wins"]["total"]["quatuor"]}

            : Total :
        Break Bed: {bedwarsStats["breakBed"]["total"]["all"]}
        Games Played: {bedwarsStats["played"]["total"]["all"]}
        Final Kills: {bedwarsStats["finalKills"]["total"]["all"]}
        Final Deaths {bedwarsStats["finalDeaths"]["total"]["all"]}
        Kills: {bedwarsStats["kills"]["total"]["all"]}
        Bed Lost: {bedwarsStats["lostBed"]["total"]["all"]}
        Deaths: {bedwarsStats["deaths"]["total"]["all"]}
        Wins: {bedwarsStats["wins"]["total"]["all"]}
        Looses: {bedwarsStats["played"]["total"]["all"]-bedwarsStats["wins"]["total"]["all"]}
        ''')
        input()
        menu(data, serverInfo)

    if choice == "3":
        
        clanData = data["player"]["clan"]
        print(f"""
        
                : CLAN :
        Name: {clanData["name"]}
        ID: {clanData["id"]}
        TAG: {clanData["tag"]}
        Status: {clanData["status"]}
        Creation Date: {datetime.datetime.fromtimestamp(clanData["createdAt"] / 1000)}


                :  XP  :
        Level: {clanData["level"]}
        XP: {clanData["experience"]}
        Required XP: {clanData["requiredExperience"]}
        Daily XP: {clanData["dailyExperience"]}
        Monthly XP: {clanData["monthlyExperience"]}
        Total XP: {clanData["totalExperience"]}
        """)
        input()
        menu(data, serverInfo)
        
    if choice == "4":
        username = input('\n\n\n\n                    [>] Player Name: ')
        r = requests.get(url=f"https://api.rinaorc.com/player/{username}", headers=header)
        data = r.json()
        menu(data, serverInfo)



while True:
    
    try:
        menu(data, serverInfo)
    except:
        
        input(' An error has occurred. There is many reasons for that:\n 1) Rinaorc\'s API is down.\n 2) The user provided has never logged on Rinaorc.\n 3) Your API Key is not valid, change it in the settings.')
