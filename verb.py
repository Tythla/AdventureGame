from player import Player
from load import map
from dsc_print import show

def go(direction = None):
    if direction == None:
        print('You cannot go nowhere')
    elif direction in map[Player.position]['exits'].keys():
        Player.position = map[Player.position]['exits'][direction]
        print('You go ' + direction + '.')
        show(map[Player.position])
    else:
        print('There is no way to go '+direction)

def look():
    show(map[Player.position])
