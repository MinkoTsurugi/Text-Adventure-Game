import os

#starting menu
def prompt():
    print("\t\t\tWelcome to my game\n\n\
          You must find the boss and defeat it.\n\n\
          Move:\t 'go {direction}' (travel north, south, east, west)\n\n\
          \t 'get {item}' (add nearby item to inventory)")

    input("Press any key to continue...")

#clears screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#map
map = {
    'Starting Area': {'North': 'Forest Route', 'East': 'Cave Route', 'West': 'Beach Route'},
    ##Beach Route
    'Beach Route': {'North': 'Beach Area I', 'Item': 'Sword'},
    'Beach Area I': {'North': 'Beach Area II', 'South': 'Beach Route', 'Item': 'Fishing Rod', 'Monster': ''},
    'Beach Area II': {'North': 'Beach Area V', 'South': 'Beach Area I', 'West': 'Beach Area III', 'Item': 'Potion'},
    'Beach Area III': {'North': 'Beach Area IV', 'East': 'Beach Area II'},
    'Beach Area IV': {'South': 'Beach Area III', 'East': 'Beach Area V', 'Item': 'Armor'},
    'Beach Area V': {'North': 'Beach Boss', 'Monster': ''},
    'Beach Boss': {'Boss': ''},
    ##Forest Route
    'Forest Route': {'North': 'Forest Area I', 'Item': 'Sword', 'Monster': ''},
    'Forest Area I': {'North': 'Forest Area III', 'South': 'Forest Route', 'East': 'Forest Area II', 'Monster': ''},
    'Forest Area II': {'West': 'Forest Area I', 'Item': 'Armor'},
    'Forest Area III': {'North': 'Forest Boss', 'South': 'Forest Area I', 'Item': 'Potion'},
    'Forest Boss': {'Boss': ''},
    ##Cave Route
    'Cave Route': {'North': 'Cave Area I', 'Item': 'Sword'},
    'Cave Area I': {'North': 'Cave Area II', 'South': 'Cave Route', 'Monster': ''},
    'Cave Area II': {'North': 'Cave Area III', 'South': 'Cave Area I'},
    'Cave Area III': {'North': 'Cave Area V', 'South': 'Cave Area II', 'East': 'Cave Area IV', 'Item': 'Armor'},
    'Cave Area IV': {'North': 'Special Boss', 'West': 'Cave Area III'},
    'Cave Area V': {'North': 'Cave Boss', 'South': 'Cave Area III', 'Item': 'Potion'},
    'Special Boss': {'Hidden Boss': ''},
    'Cave Boss': {'Boss': ''}
    }

#vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#inventory
inventory = []

#current room

current_room = "Starting Area"

#last move
msg = ""

clear()
prompt()

while True:
    clear()

    #Display info
    print(f"You are in the {current_room}\n Inventory: {inventory}\n{'-' * 27}")

    #Display msg
    print(msg)

    if "Item" in map[current_room].keys():

        nearby_item = map[current_room]["Item"]

        if nearby_item not in inventory:

            #plural
            if nearby_item[-1] == 's':
                print(f"YOu see {nearby_item}")
            
            #singular starts with vowel
            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            #singular starts with consanant
            else:
                print(f"You see a {nearby_item}")

    if "Boss" in map[current_room].keys():

        if "Sword" and "Armor" not in inventory:
            print("You Lose")
            input("Press any key to continue...")
            break
        else:
            print("You Win")
            input("Press any key to continue...")
            break

    elif "Hidden Boss" in map[current_room].keys():
        if "Sword" and "Armor" not in inventory:
            print("You Lose")
            break
        else:
            print("You Win")
            break

    user_input = input("Enter your move: \n")

    next_move = user_input.split(' ')

    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()


    if action == "Go":

        try:
            current_room = map[current_room][direction]
            msg = f"You travel {direction}."
        
        except:
            msg = "You can't go that way."
        
    elif action == "Get":

        try:
            if item == map[current_room]["Item"]:
                if item not in inventory:
                    inventory.append(map[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}."
            
            else:
                msg = f"Can't find {item}"

        except:
            msg = f"Can't find {item}"
        
    elif action == "Exit":
        clear()
        print("Good Bye")
        break

    else:
        msg = "Invalid Command"
