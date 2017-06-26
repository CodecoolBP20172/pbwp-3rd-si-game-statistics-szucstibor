from reports import *

# Export functions


def export(file_name, export_to):
    with open(export_to, "w") as export:
        export.writelines(str(count_games(file_name))+"\n")
        export.writelines(str(decide(file_name, 1998))+"\n")
        export.writelines(str(get_latest(file_name))+"\n")
        export.writelines(str(count_by_genre(file_name, "Action-adventure"))+"\n")
        export.writelines(str(get_line_number_by_title(file_name, "Terraria"))+"\n")
        export.writelines(str(get_genres(file_name))+"\n")
        export.writelines(str(when_was_top_sold_fps(file_name))"\n")
        export.writelines(str(sort_abc(file_name))+"\n")
export("game_stat.txt", "export.txt")
