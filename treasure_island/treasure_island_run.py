# Treasure Island Game

def treasure_island_game():
    # Clears the console using ANSI escape codes
    print("\033c", end="")

    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/______/_
    *******************************************************************************
    ''')

    print("Welcome to treasure island.")
    print("Your mission is to find the treasure.")

    while True:
        direction = input(
        'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n'
        ).lower()


        if direction == "left":
            action = input(
                'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
            ).lower()

            while True:
                if action == "wait":

                    while True:
                        door = input(
                        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
                        ).lower()

                        if door == "red":
                            return "It's a room full of fire. Game Over."
                        elif door == "yellow":
                            return "You found the treasure! You Win!"
                        elif door == "blue":
                            return "You enter a room of beasts. Game Over."
                        else:
                            msg = "You chose a door that doesn't exist. Try again."
                            print(msg)

                elif action == "swim":
                    return "You get attacked by an angry trout. Game Over."
                else:
                    msg = "Invalid action. Please type 'wait' or 'swim'."
                    print(msg)

            break
        elif direction == "right":
            return "You fell into a hole. Game Over."
        else:
            msg = "You chose a path that doesn't exist. Try again."
            print("You chose a path that doesn't exist. Try again.")

if __name__ == "__main__":
    result = treasure_island_game()
    print(result)