

path = 'maps/Sort_AMSport.txt'

with open(path) as f:
    lines = f.read().splitlines()
    players = []
    for line in lines:
        if line not in players and line != '':
            players.append(line)
    players.sort()

new_path = 'maps/Map_AMSport.txt'
new_file = open(new_path, 'w')
for player in players:
    # AMSport
    new_file.write(player + ':' + player.split(' (')[0] + '\n')
    # WWin
    #temp = player.split('/')[1]
    # try:
    #     db_player = temp.split(', ')[1] + ' ' + temp.split(', ')[0]
    #     new_file.write(player + ':' + db_player + '\n')
    # except:
    #     print(temp)

new_file.close()
