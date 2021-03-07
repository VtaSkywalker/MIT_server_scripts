log_file = open('2021_3_3.log', 'r')

dic = {}
for line in log_file:
    if '破坏' in line:
        loc1 = line.find('玩家') + 3
        loc2 = line.find('在') - 1
        player_name = line[loc1:loc2]
        if '悬空地' in player_name:
            player_name = player_name[:-4]
        if player_name in dic:
            dic[player_name] += 1
        else:
            dic[player_name] = 1
print(dic)

with open('3_3.txt', 'w') as file:
    file.write(str(dic))
