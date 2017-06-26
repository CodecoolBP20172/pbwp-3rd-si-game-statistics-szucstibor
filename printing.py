# Printing functions
import pprint
from reports import *


def pretty_print(file_name):
    pp = pprint.PrettyPrinter(width=140, compact=True)
    pp.pprint(str(count_games(file_name)))
    pp.pprint(str(decide(file_name, 1998)))
    pp.pprint(str(get_latest(file_name)))
    pp.pprint(str(count_by_genre(file_name, "Action-adventure")))
    pp.pprint(str(get_line_number_by_title(file_name, "Terraria")))
    pp.pprint(str(get_genres(file_name)))
    pp.pprint(str(when_was_top_sold_fps(file_name)))
    pp.pprint(str(sort_abc(file_name)))

pretty_print("game_stat.txt")
