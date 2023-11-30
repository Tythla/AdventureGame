def show(room):
    print('> ' + room['name'])
    print(room['desc'])
    if 'items' in room and room['items']:
        print("Items: " + ", ".join(room['items']))
    print("Exits: " + ", ".join(room['exits']))
    print("Exits:", " ".join(map(str, list(room["exits"].keys()))))