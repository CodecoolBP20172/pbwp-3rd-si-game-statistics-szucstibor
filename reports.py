import csv
# Report functions
year = 0
games = []


def count_games(file_name):
    result = sum(1 for line in open(file_name))
    return result


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False
