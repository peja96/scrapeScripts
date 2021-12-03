

def remove_duplicates(file_name, dest_name):
    path = '../maps/' + file_name

    with open(path) as f:
        lines = f.read().splitlines()
        players = []
        for line in lines:
            if line not in players and line != '':
                players.append(line)
        players.sort()

    new_path = '../maps/' +dest_name
    new_file = open(new_path, 'w')
    for player in players:
        new_file.write(player + '\n')

    new_file.close()


if __name__ == "__main__":
    remove_duplicates('Map_WWin.txt', 'Map_WWin.txt')
