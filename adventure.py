from player import Player
from load import map
from dsc_print import show
from verb import *

Player.position = 0
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
        