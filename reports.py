import csv
# Report functions


def games_to_list(file_name):
    games = []
    with open(file_name) as stats:
        for line in csv.reader(stats, delimiter="\t"):
            games.append(line)
        return games


def count_games(file_name):
    result = sum(1 for line in open(file_name))
    return result


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False


def get_latest(file_name):
    games = games_to_list(file_name)
    latest = 0
    for iteration in range(len(games)):
        if int(games[iteration][2]) > int(latest):
            latest = games[iteration][2]
    for iteration in range(len(games)):
        if games[iteration][2] == latest:
            result = str(games[iteration][0])
            return result


def count_by_genre(file_name, genre):
    games = games_to_list(file_name)
    result = 0
    for iteration in range(len(games)):
        if genre == games[iteration][3]:
            result += 1
    return result


def get_line_number_by_title(file_name, title):
    games = games_to_list(file_name)
    result = 0
    for iteration in range(len(games)):
        if title == games[iteration][0]:
            result = int(iteration + 1)
            break
    return result


def get_genres(file_name):
    result = []
    games = games_to_list(file_name)
    for iteration in range(len(games)):
        if games[iteration][3] not in result:
            result.append(games[iteration][3])
    result = sorted(result, key=str.lower)
    return result


def when_was_top_sold_fps(file_name):
    games = games_to_list(file_name)
    best_seller = 0
    fpses = []
    for iteration in range(len(games)): 
        if games[iteration][3] == "First-person shooter": 
            fpses.append(games[iteration])
    for iteration in range(len(fpses)):
        if float(fpses[iteration][1]) > float(best_seller):
            (best_seller) = (fpses[iteration][1])
    for iteration in range(len(fpses)):
        if best_seller == fpses[iteration][1]:
            result = int(fpses[iteration][2])
            return result
