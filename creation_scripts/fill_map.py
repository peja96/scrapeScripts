
import_path = '../maps/Sort_WWin.txt'
map_path = '../maps/Map_WWin.txt'
export_path = '../maps/Map_WWin.txt'

with open(import_path) as f:
    lines = f.read().splitlines()
    players = []
    for line in lines:
        if line not in players and line != '':
            players.append(line)
    players.sort()

with open(map_path) as f:
    lines = f.read().splitlines()
    mapped_players = []
    for line in lines:
        if line not in mapped_players and line != '':
            mapped_players.append(line)
    mapped_players.sort()

for player in players:
    if not any(player in string for string in mapped_players):
        mapped_players.append(player + ":")

mapped_players.sort()

new_file = open(export_path, 'w')
for player in mapped_players:
    new_file.write(player + '\n')

new_file.close()
