import csv
# Report functions
year = 0
games = []


def games_to_lists(file_name):
    global games
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