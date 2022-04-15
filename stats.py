import requests
import json
from os import system
system("title Stats Rinaorc by Krystal#6960")
system("mode 78, 10")
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

def menu():
    clear()
    system("mode 78, 10")
    choice = input("\n\n\n                                Choose Info:\n        [1] User Info        [2] BedWars Info        [3] Server Info\n\n                                 Choice: ")
    clear()
    if choice == "1":
        system("mode 78, 200")
        playerData = data["player"]
        if playerData["isOnline"] == True: online="Online"
        else: online="Offline"
        print(f'''
            : Player Information :
            
        Rinaorc ID: {playerData["id"]}
        Minecraft UUID: {playerData["uuid"]}
        Rank: {playerData["rank"]["name"]}
        Status: {online}
        Connection Method: {playerData["connectionMethod"]}
        
        Discord ID: {playerData["links"]["discord"]["user_id"]}
        Booster: {playerData["hasBoost"]}
        
        Aura: {playerData["aura"]}''')
        input()
    if choice == "2":
        system("mode 78, 500")
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

    if choice == "3":
        system("mode 50, 35")
        print(f'''
            : Server Info :
        Registered Players: {serverInfo["registeredPlayers"]}
        Active Player: {serverInfo["activePlayers"]}
        Online Players: {serverInfo["onlinePlayers"]}

            :     BAN     :
        Total Bans: {serverInfo["punishments"]["bans"]["totalBans"]}
        Monthly Bans: {serverInfo["punishments"]["bans"]["monthlyBans"]}
        Weekly Bans: {serverInfo["punishments"]["bans"]["weeklyBans"]}
        
            :     MUTE    :
        Total Mutes: {serverInfo["punishments"]["mutes"]["totalMutes"]}
        Monthly Mutes: {serverInfo["punishments"]["mutes"]["monthlyMutes"]}
        Weekly Mutes: {serverInfo["punishments"]["mutes"]["weeklyMutes"]}
        
           :PLAYERS IN GAME:
        BedWars: {serverInfo["games"]["bedwars"]["players"]}
        Caveaux: {serverInfo["games"]["caveaux"]["players"]}
        Free Build: {serverInfo["games"]["freebuild"]["players"]}
        Golem Rush: {serverInfo["games"]["golemrush"]["players"]}
        Gun Wars: {serverInfo["games"]["gunwars"]["players"]}
        Lobby: {serverInfo["games"]["lobbyMain"]["players"]}
        Parkour: {serverInfo["games"]["parkour"]["players"]}
        Pixel Perfect: {serverInfo["games"]["pixelperfect"]["players"]}
        Practice: {serverInfo["games"]["practice"]["players"]+serverInfo["games"]["pvpbox"]["players"]+serverInfo["games"]["pvpenchants"]["players"]}
        Sheep Wars: {serverInfo["games"]["sheepwars"]["players"]}
        Sky Wars: {serverInfo["games"]["skywars"]["players"]}
        Smash: {serverInfo["games"]["smash"]["players"]}
        The Purge: {serverInfo["games"]["thepurge"]["players"]}
        UHC: {serverInfo["games"]["uhc"]["players"]}
        Warfare: {serverInfo["games"]["warfare"]["players"]}
        Warzone: {serverInfo["games"]["warzone"]["players"]}''')
        input()
    
while True:
    system("mode 78, 10")
    try: menu()
    except: 
        system("mode 78, 10")
        input(' An error has occurred. There is many reasons for that:\n 1) Rinaorc\'s API is down.\n 2) The user provided has never logged on Rinaorc.\n 3) Your API Key is not valid, change it in the settings.')