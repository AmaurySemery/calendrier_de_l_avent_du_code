import csv
import time

start = time.time()

def create_dict_from_string(item):
    if item[1] in ['1','2','3','4','5','6','7','8','9','0']:
        return {item[2:]: int(item[:2])}
    else:
        return {item[1:]: int(item[0])}

list_games = []

with open('python/day_2/input.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        new_row = [word.replace(' ', '') for word in row]
        columns = [item.split(":") for item in new_row]
        del(columns[0][0])
        list_test = []
        for i in columns:
            data = [item.split(",") for item in i]
            list_test.append(data[0])
        final_convert = [[create_dict_from_string(word) for word in sublist] for sublist in list_test]
        list_games.append(final_convert)

def testing_colors(color,row):
    color_value = [sub_dict.get(color, 0) for sublist in row for sub_dict in sublist if color in sub_dict]
    return color_value

def testing_games(list_games):
    i = 1
    list_games_playable = []
    for row in list_games:
        green = testing_colors("green",row)
        red = testing_colors("red",row)
        blue = testing_colors("blue",row)
        #print('green = ',green, ' ; red = ',red,' : blue = ',blue)
        if all(x <= 13 for x in green) and all(x <= 12 for x in red) and all(x <= 14 for x in blue):
            list_games_playable.append(i)

        i +=1
    
    #print(list_games_playable)
    print(sum(list_games_playable))

testing_games(list_games)

end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {elapsed:.2}ms')