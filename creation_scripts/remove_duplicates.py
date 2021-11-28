import os.path
from os import listdir
from os.path import isfile, join

path = '../maps/Meridian.txt'

with open(path) as f:
    lines = f.read().splitlines()
    players = []
    for line in lines:
        if line not in players and line != '':
            players.append(line)
    players.sort()

new_path = '../maps/Sort_Meridian.txt'
new_file = open(new_path, 'w')
for player in players:
    new_file.write(player + '\n')

new_file.close()
