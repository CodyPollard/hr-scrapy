import json_lines
from datetime import datetime
from dateutil.parser import parse


def parse_games():
    # Reorder list chronologically
    ordered_gamelist = {}
    with open_data('gamelinks_ducks.jl') as f:
        for game in json_lines.reader(f):
            x = parse(game['game_date'])
            print(type(x))
            # print(game['game_date'])
            # count_players(game['skater_list'])


def open_data(file):
    return open(file, 'rb')


def count_players(player_list):
    for player in player_list:
        print(player)


if __name__ == '__main__':
    parse()
