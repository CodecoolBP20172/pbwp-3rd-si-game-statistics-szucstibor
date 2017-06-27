import csv
import re
# Report functions


def games_to_list(file_name):
    games = []
    with open(file_name) as stats:
        for line in csv.reader(stats, delimiter="\t"):
            games.append(line)
        return games


def get_most_played(file_name):
    games = games_to_list(file_name)
    best_seller = 0
    for iteration in range(len(games)):
        if float(games[iteration][1]) > float(best_seller):
            (best_seller) = (games[iteration][1])
    for iteration in range(len(games)):
        if best_seller == games[iteration][1]:
            result = games[iteration][0]
            return result


def sum_sold(file_name):
    games = games_to_list(file_name)
    result = 0
    for iteration in range(len(games)):
        result += float(games[iteration][1])
    return result


def get_selling_avg(file_name):
    games = games_to_list(file_name)
    total_selling = 0
    result = 0
    for iteration in range(len(games)):
        total_selling += float(games[iteration][1])
    result = total_selling / len(games)
    return result


def count_longest_title(file_name):
    games = games_to_list(file_name)
    result = 0
    title = ""
    for iteration in range(len(games)):
        title = games[iteration][0]
        if len(title) > result:
            result = len(title)
    return result


def get_date_avg(file_name):
    games = games_to_list(file_name)
    total_date = 0
    result = 0
    for iteration in range(len(games)):
        total_date += float(games[iteration][2])
    result = round(total_date / len(games), 0)
    return result


def get_game(file_name, title):
    games = games_to_list(file_name)
    result = []
    for iteration in range(len(games)):
        if title == games[iteration][0]:
            for appending in range(len(games[iteration])):
                if appending == 1:
                    result.append(float(games[iteration][appending]))
                elif appending == 2:
                    result.append(int(games[iteration][appending]))
                else:
                    result.append(games[iteration][appending])
    return result
