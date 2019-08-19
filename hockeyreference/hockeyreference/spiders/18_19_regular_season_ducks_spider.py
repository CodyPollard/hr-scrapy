import scrapy
from dateutil.parser import parse
from hockeyreference.items import GamedayRoster, Skater


class TeamsSpider(scrapy.Spider):
    name = "reg_season"

    def start_requests(self):
        urls = ['https://www.hockey-reference.com/teams/ANA/2019_gamelog.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Check and scape if page is gamelog
        for row in response.css("table#tm_gamelog_rs>tbody>tr"):
            game_url = row.xpath("td//a/@href").get()
            if game_url is not None:
                print('FOLLOWING GAME LINK')
                yield response.follow(game_url, callback=self.parse_games)

    def parse_games(self, response):
        # Check and scrape if page is individual game
        roster = GamedayRoster()
        skater_list = ['']
        # Get game date
        meta = response.css("div.scorebox_meta")
        date = meta.xpath("div//text()").get()
        if parse(date):
            roster['game_date'] = meta.xpath("div//text()").get()
        else:
            print('INVALID DATE %s' % date)

        # Find skater list
        skater_table = response.css("table#ANA_skaters>tbody")
        for row in skater_table.xpath("tr"):
            # Append skater to skater_list for yield later
            skater_list.append(row.xpath("td[1]//text()").get())
        roster['skater_list'] = skater_list

        yield roster




