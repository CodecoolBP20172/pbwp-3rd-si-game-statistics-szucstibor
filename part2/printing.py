from reports import *
import pprint
# Printing functions


def pretty_print(file_name):
    pp = pprint.PrettyPrinter(width=140, compact=True)
    pp.pprint(str(games_to_list(file_name)))
    pp.pprint(str(get_most_played(file_name)))
    pp.pprint(str(sum_sold(file_name)))
    pp.pprint(str(get_selling_avg(file_name)))
    pp.pprint(str(count_longest_title(file_name)))
    pp.pprint(str(get_date_avg(file_name)))
    pp.pprint(str(get_game(file_name, "Terraria")))

pretty_print("game_stat.txt")