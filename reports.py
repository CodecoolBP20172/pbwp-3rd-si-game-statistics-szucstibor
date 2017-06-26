import csv
# Report functions


def games_to_lists(file_name):
    with open(file_name) as stats:
        for line in csv.reader(stats, dialect="excel-tab"):
            games.append(line)


def count_games(file_name):
    result = sum(1 for line in open(file_name))
    return result


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False


def get_latest(file_name):
    games_to_lists(file_name)
    latest = 0
    for iteration in range(len(games)):
        if int(games[iteration][2]) > int(latest):
            latest = games[iteration][2]
    for iteration in range(len(games)):
        if games[iteration][2] == latest:
            result = str(games[iteration][0])
            return result


def count_by_genre(file_name, genre):
    games_to_lists(file_name)
    result = 0
    for iteration in range(len(games)):
        if genre == games[iteration][3]:
            games[iteration]
            result += 1
    print(result)
    return result

count_by_genre("game_stat.txt", "First-person shooter")
