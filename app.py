import constants
import sys

teams_2 = constants.TEAMS
players_2 = constants.PLAYERS
exp_player = []
notexp_player = []
Panthers = []
Bandits = []
Warriors = []


def clean_data():
    for player in constants.PLAYERS:
        player["height"] = int(player["height"][0:2])
        player["guardians"] = (", ".join(player["guardians"].split(" and ")))
        if player["experience"] == "YES":
            player["experience"] == True
            exp_player.append(player)
        elif player["experience"] == "NO":
            player["experience"] == False
            notexp_player.append(player)
    return teams_2


def balance_teams():
    teams = [Panthers, Bandits, Warriors]
    number_teams = (len(teams))
    for num in range(len(exp_player)):
        teams[num % number_teams].append(exp_player[num])
    for num in range(len(notexp_player)):
        teams[num % number_teams].append(notexp_player[num])


def display_stats(team):
    total_players = len(team)
    players_names = []
    guardians_names = []
    experience_count = 0
    notexperience_count = 0
    team_height = 0
    for player in team:
        players_names.append(player["name"])
        guardians_names.append(player["guardians"])
        team_height += player["height"]
        if player["experience"] == True:
            experience_count += 1
        else:
            notexperience_count += 1
    average_height = round(team_height / len(team))
    print("Total Players: {}".format(total_players))
    print("Experienced Players: {}".format(experience_count))
    print("Rookies: {}".format(notexperience_count))
    print("Average Height: {}".format(average_height))
    print("\nPLAYERS:  ")
    print(", ".join(players_names))
    print("\nGUARDIANS:  ")
    print(", ".join(guardians_names), "\n")


def Menu():
    print("BASKETBALL STATS TOOL\n")
    print("-----MENU-----\n")
    print("1)  Display Team Stats")
    print("2)  Quit")
    print("Pick an option: ")
    while True:
        try:
            option1 = int(input("For continue press 1 for quit press 2: "))
            if option1 < 1 or option1 > 2:
                print("\nPlease retry entry. Select 1 or 2\n")
                continue
        except ValueError:
            print("\nPlease retry entry. Select 1 or 2\n")
        else:
            if option1 == 1:
                print("\n")
                print("-----TEAMS-----\n")
                print("1: Panthers")
                print("2: Bandits")
                print("3: Warriors\n")
                try:
                    option2 = int(input("Select team: "))
                    if option2 < 1 or option2 > 3:
                        print("\nNot a valid selection. Please, try again\n")
                        continue
                except ValueError:
                    print ("\nNot a valid selection. Please, try again\n")
                else:
                    if option2 == 1:
                        print("\n____PANTHERS____")
                        display_stats(Panthers)
                    elif option2 == 2:
                        print("\n____BANDITS____")
                        display_stats(Bandits)
                    elif option2 == 3:
                        print("\n____Warriors____")
                        display_stats(Warriors)
            elif option1 == 2:
                break
    sys.exit("\nExited tool\n")


            

if __name__ == "__main__":
    clean_data()
    balance_teams()
    Menu()
    display_stats()
