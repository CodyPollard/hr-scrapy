import scrapy


class Skater(scrapy.Item):
    # Player name and stats from skater_table
    name = scrapy.Field()
    age = scrapy.Field()
    pos = scrapy.Field()
    gp = scrapy.Field()
    # Scoring
    goals = scrapy.Field()
    assists = scrapy.Field()
    points = scrapy.Field()
    pm = scrapy.Field()
    pim = scrapy.Field()
    # Goal specifics
    ev_goals = scrapy.Field()
    pp_goals = scrapy.Field()
    sh_goals = scrapy.Field()
    gw_goals = scrapy.Field()
    # Assist specifics
    ev_assists = scrapy.Field()
    pp_assists = scrapy.Field()
    sh_assists = scrapy.Field()
    # Shots
    shots = scrapy.Field()
    shot_percent = scrapy.Field()
    # Ice time
    toi = scrapy.Field()
    atoi = scrapy.Field()
    # Misc
    blk = scrapy.Field()
    hit = scrapy.Field()
    fow = scrapy.Field()
    fol = scrapy.Field()
    fo_percent = scrapy.Field()


class Team(scrapy.Item):
    name = scrapy.Field()
    # Have list of skaters under team?
    # players = Skater()
