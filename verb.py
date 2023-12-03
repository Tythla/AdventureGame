from player import Player
from load import map
from dsc_print import show
import sys
import inspect

directions = {
    "north": "north", "n": "north",
    "south": "south", "s": "south",
    "east": "east", "e": "east",
    "west": "west", "w": "west",
    "northeast": "northeast", "ne": "northeast",
    "northwest": "northwest", "nw": "northwest",
    "southeast": "southeast", "se": "southeast",
    "southwest": "southwest", "sw": "southwest"
    # Add more directions or abbreviations as needed
}

def go(direction=None):
    if direction is None:
        print('You cannot go nowhere.')
        return

    # Standardizing the direction input
    direction = direction.lower()
    if direction in directions:  # 'directions' is your mapping dictionary
        direction = directions[direction]

    # Check if the direction is a valid exit in the current room
    current_room = map[Player.position]
    if direction in current_room['exits']:
        Player.position = current_room['exits'][direction]
        print(f'You go {direction}.')
        show(map[Player.position])
    else:
        print(f'There is no way to go {direction}.')

def parse_command(command):
    words = command.split()
    action = words[0].lower()

    # Handling direction commands (both explicit and implicit)
    if action in directions or action == "go":
        direction = directions.get(action) or words[1].lower() if len(words) > 1 else None
        go(direction)
        
    else:
        print("I don't understand that command.")


def look():
    show(map[Player.position])

def get(item=None):
    if item is None:
        print("You must specify what you want to get.")
        return

    current_room = map[Player.position]

    # Check if the room has an 'items' field and the item is in the room
    if 'items' in current_room and item in current_room['items']:
        # Remove the item from the room
        current_room['items'].remove(item)

        # Add the item to the player's inventory
        Player.inventory.append(item)
        print(f"You picked up the {item}.")
    else:
        print(f"There is no {item} here to get.")

def g():
    item_get = input()
    get(item_get)

def quit():
    print("Thank you for playing. Goodbye!")
    sys.exit(0)

def drop(item=None):
    if item is None:
        print("You must specify what you want to drop.")
        return

    # Check if the item is in the player's inventory
    if item in Player.inventory:
        # Remove the item from the player's inventory
        Player.inventory.remove(item)

        # Add the item to the current room's items
        current_room = map[Player.position]
        if 'items' not in current_room:
            current_room['items'] = []
        current_room['items'].append(item)

        print(f"You dropped the {item}.")
    else:
        print(f"You don't have {item} in your inventory.")

def d():
    item_drop = input()
    drop(item_drop)

verb_descriptions = {
    "go": "Move to a location.",
    "get": "Pick up an item.",
    "look": "Check your location and where you can move to.",
    "drop": "Remove an item from your inventory.",
    "quit": "Leave the game."
}

def help():
    print("Available commands:")
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isfunction(obj) and name in verb_descriptions:
            description = verb_descriptions[name]
            verb_name = name + (" ..." if inspect.signature(obj).parameters else "")
            print(f" - {verb_name}: {description}")
