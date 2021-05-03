import constants
import copy

print("BASKETBALL TEAM STATS TOOL") 

def convert_height():
    for player in formatted_list:
        player["height"].split()
        player["height"] = player["height"][0:2]
        player["height"] = int(player["height"])

def convert_experiences():
    for player in formatted_list:
        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False

def menu():
    global menu_option
    print("\n----MENU----")
    print("\nHere are your choices:")
    print("A) Display Team Stats \nB) Quit \n")

    while True:
        try:
            menu_option = input("Enter an option: ")
            if menu_option == "A" or menu_option == "B":
                break
            else:
                print("Not a valid input. Try again...")
        except ValueError:
            print("Not a valid input. Try again...")
  
def team_select():
    global team_option
    global team_selected
    print("\n----Teams----")
    print("\nA) Panthers \nB) Bandits \nC) Warriors \n")

    while True:
        try:
            team_option = input("Select a team: ")
            if team_option == "A" or team_option == "B" or team_option == "C":
                break
            else:
                print("Not a valid input. Try again...")
        except ValueError:
            print("Not a valid input. Try again...")

def player_assign():
    global Panthers
    global Bandits
    global Warriors
    Panthers =  formatted_list[0::3]
    Bandits = formatted_list[1::3]
    Warriors = formatted_list[2::3]

def team_status(team_option):
    experienced_count = 0
    inexperienced_count = 0
    height = []

    if team_option == "A":
        team_option = "Panthers"
        team_list = Panthers
    elif team_option == "B":
        team_option = "Bandits"
        team_list = Bandits
    else:
        team_option = "Warriors"
        team_list = Warriors

    print(f"\nTeam: {team_option}")
    print("-" * 24)

    print("Total players:", len(team_list))
    
    for player in team_list:
        if player["experience"] == True:
            experienced_count += 1
    print(f"Total experienced players: {experienced_count}")

    for player in team_list:
        if player["experience"] == False:
            inexperienced_count += 1
    print(f"Total inexperienced players: {inexperienced_count}")

    for player in team_list:
        player_height = []
        height.append(player["height"])
        total_height = sum(height)
        average_height = total_height / len(team_list)
    print(f"Average height of players: {average_height}")
    
    print("\nPlayer names:")
    for player in team_list:
            print(player["name"], end=", ")

    print("\n\nPlayer guardians:")
    for index, player in enumerate(team_list,1):
            print(f"{index}", player["guardians"])

def continue_or_quit():
    global continue_or_quit_option
    while True:
        try:
            continue_or_quit_option = input("\nPress (C) to continue to the menu or (Q) to quit: ")
            if continue_or_quit_option == "C" or continue_or_quit_option == "Q":
                break
            else:
                print("Not a valid input. Try again...")
        except ValueError:
            print("Not a valid input. Try again...")

def end_tool():
    print("\nGOODBYE")
    print("-"*24)

if __name__ == "__main__":
    formatted_list = copy.deepcopy(constants.PLAYERS)
    player_assign()
    convert_height()
    convert_experiences()
    while True:
        menu()
        if menu_option == "A":
            team_select()
            team_status(team_option)
            continue_or_quit()
            if continue_or_quit_option == "Q":
                end_tool()
                break
        else:
            end_tool()
            break   