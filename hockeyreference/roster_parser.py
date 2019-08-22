import json_lines, json
from datetime import datetime, date
from dateutil.parser import parse


class Game(object):

    def __init__(self, gamedate, roster):
        self.gamedate = gamedate
        self.roster = roster


class Player(object):

    def __init__(self, name):
        self.name = name
        self.games_missed = []
        self.games_played = []

    def get_game_breakdown(self):
        """Returns list of all games a player missed in a given season"""
        # Open season data and add games to list if self.player was not present
        with open_data('output/ducks_18-19_skaters.json') as f:
            data = json.load(f)
            for game in data:
                if self.name not in game['roster']:
                    self.games_missed.append(game['gamedate'])
                else:
                    self.games_played.append(game['gamedate'])
            f.close()

    def missed_streaks(self):
        pass

    def export_player(self):
        """Runs all functions above and exports player to individual JSON files"""
        # Pulling data
        self.get_game_breakdown()
        # Exporting
        file_name = '18-19-%s' % self.name.replace(' ', '-').lower()
        with open('output/individual/%s.json' % file_name, 'w') as f:
            json.dump(self.__dict__, f, indent=4)


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
    with open('output/ducks_18-19_skaters.json', 'w') as rs:
        json.dump([ob.__dict__ for ob in all_games], rs, indent=4)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


# Sanitized JSON Data #
def get_all_players():
    all_players = []
    with open_data('output/ducks_18-19_skaters.json') as f:
        data = json.load(f)
        for game in data:
            for player in game['roster']:
                if player not in all_players:
                    all_players.append(player)
        f.close()
    return all_players


def export_all_players():
    all_players = get_all_players()
    for player in all_players:
        Player(player).export_player()


def convert_game_dates():
    numbered_games = []
    with open_data('gamelinks_ducks.jl') as f:
        for i, game in enumerate(json_lines.reader(f)):
            numbered_games.append('{}#{}'.format(i+1, game['game_date']))
        f.close()
    to_json('output/18-19_schedule.json', numbered_games)
    print(numbered_games)


def to_json(file, data):
    with open(file, 'w') as rs:
        json.dump(data, rs, indent=4)


if __name__ == '__main__':
    # parse_raw()
    # # count_players()
    # Player('Hampus Lindholm')
    convert_game_dates()
    # export_all_players()
