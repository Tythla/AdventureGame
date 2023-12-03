from player import Player
from load import map
from dsc_print import show
from verb import *

Player.position = 0
Player.inventory = []
steps = 0

try:
    map[Player.position]
except:
    print('No valid map data')
    exit()
show(map[Player.position])

if steps>50:
    print('You starved amd died')
    exit()

while True:
    try:
        command=input('What would you like to do?')
    except EOFError:
        print("Use 'quit' to exit.")
        continue

    if command.lower() == "quit":
        print("Goodbye!")
        exit()
    else:
        command = command.lower().split(' ', 1)
        if len(command) == 1: 
            if command[0] in verb_dict_1:
                verb_dict_1[command[0]]()
            elif command[0] in verb_dict_2:
                verb_dict_2[command[0]]()
            else:
                print("Plase enter a right verb.")
        elif len(command) == 2 and command[0] in verb_dict_2:
            if command[0] in verb_dict_2:
                verb_dict_2[command[0]](command[1]) # this's like go('east')
            else:
                print("Plase enter a right verb.")
        else:
            print("Plase enter a right verb.")

    if Player.position==5:
        if 'a old scroll' in Player.inventory:
            print('You defeated the boss! Congrat!')
        else:
            print('The boss killed you. Game over')
            exit()