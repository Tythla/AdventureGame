import sys
import json

if len(sys.argv) <2 :
    print('The file name cannot be empty')
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        map = json.load(filename)
except:
    print('file name not valid')
    exit()