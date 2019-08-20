import json_lines, json
from datetime import datetime, date
from dateutil.parser import parse


class Game(object):

    def __init__(self, gamedate, roster):
        self.gamedate = gamedate
        self.roster = roster


# Misc #
def open_data(file):
    return open(file, 'rb')


# Raw #
def parse_raw():
    """Parses raw JL data and formats for use later in a new JSON file."""

    # Reorder list chronologically
    game_dates = []
    all_games = []
    with open_data('gamelinks_ducks.jl') as f:
        for game in json_lines.reader(f):
            # print(game['game_date'])
            game_dates.append(parse(game['game_date']))
        f.close()
    # Sort games
    game_dates.sort()
    # Compare and read to dict with rosters
    for x in game_dates:
        with open_data('gamelinks_ducks.jl') as f:
            for g in json_lines.reader(f):
                if x == parse(g['game_date']):
                    temp_game = Game(g['game_date'], g['skater_list'])
                    all_games.append(temp_game)
            f.close()
    # Write ordered list to JSON
    with open('ducks_18-19_skaters.json', 'w') as rs:
        json.dump([ob.__dict__ for ob in all_games], rs, indent=4)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


# Sanitized JSON Data #
def count_players():
    with open_data('ducks_18-19_skaters.json') as f:
        data = json.load(f)
        for game in data:
            print(game['gamedate'])


if __name__ == '__main__':
    # parse_raw()
    count_players()
