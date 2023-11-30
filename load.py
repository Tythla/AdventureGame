import sys
import json

if len(sys.argv)==0:
    print('The file name cannot be empty')
    sys.exit()

filename = sys.argv[0]

try:
    with open(filename):
        map = json.load(filename)
except:
    print('file name not valid')
    exit()