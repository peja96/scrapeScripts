import os.path
from os import listdir
from os.path import isfile, join

path = os.path.join('C:', os.sep, 'Users', 'Nikola', 'Desktop', 'euroliga_slike')
only_files = [f for f in listdir(path) if isfile(join(path, f))]

for file in only_files:
    old_name = file
    new_name = file.split('-')[0] + '.png'
    os.renames(path + os.sep + old_name, path + os.sep + new_name)
    print(path + os.sep + new_name)
