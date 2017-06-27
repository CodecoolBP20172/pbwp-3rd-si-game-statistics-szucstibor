from reports import *
# Export functions


def export(file_name, export_to):
    with open(export_to, "w") as export:
        export.writelines(str(games_to_list(file_name))+"\n")
        export.writelines(str(get_most_played(file_name))+"\n")
        export.writelines(str(sum_sold(file_name))+"\n")
        export.writelines(str(get_selling_avg(file_name))+"\n")
        export.writelines(str(count_longest_title(file_name))+"\n")
        export.writelines(str(get_date_avg(file_name))+"\n")
        export.writelines(str(get_game(file_name, "Terraria"))+"\n")

export("game_stat.txt", "export.txt")
