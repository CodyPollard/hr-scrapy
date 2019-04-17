import scrapy
from hockeyreference.items import Skater, Team


class TeamsSpider(scrapy.Spider):
    name = "teams"

    def start_requests(self):
        urls = []
        team_names = [
            'ANA', 'ARI', 'BOS', 'BUF', 'CAR', 'CGY', 'CHI', 'CBJ', 'COL', 'DAL', 'DET',
            'EDM', 'FLA', 'LAK', 'MIN', 'MTL', 'NSH', 'NJD', 'NYI', 'NYR', 'OTT',
            'PHI', 'PIT', 'SJS', 'STL', 'TBL', 'TOR', 'VAN', 'VGK', 'WPG', 'WSH',
        ]
        for t in team_names:
            urls.append('https://www.hockey-reference.com/teams/%s/2019.html' % t)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        skater_table = response.css("table#skaters>tbody")
        skater = Skater()
        # team = Team()

        # team['name'] = response.url.split('/')[-2]
        for row in skater_table.xpath("tr"):
            try:
                skater['name'] = row.xpath("td[1]//text()").get()
                skater['age'] = row.xpath("td[2]//text()").get()
                skater['pos'] = row.xpath("td[3]//text()").get()
                skater['gp'] = row.xpath("td[4]//text()").get()
                # Scoring
                skater['goals'] = row.xpath("td[5]//text()").get()
                skater['assists'] = row.xpath("td[6]//text()").get()
                skater['points'] = row.xpath("td[7]//text()").get()
                skater['pm'] = row.xpath("td[8]//text()").get()
                skater['pim'] = row.xpath("td[9]//text()").get()
                # Goal specs
                skater['ev_goals'] = row.xpath("td[10]//text()").get()
                skater['pp_goals'] = row.xpath("td[11]//text()").get()
                skater['sh_goals'] = row.xpath("td[12]//text()").get()
                skater['gw_goals'] = row.xpath("td[13]//text()").get()
                # Assist specs
                skater['ev_assists'] = row.xpath("td[14]//text()").get()
                skater['pp_assists'] = row.xpath("td[15]//text()").get()
                skater['sh_assists'] = row.xpath("td[16]//text()").get()
                # Shots
                skater['shots'] = row.xpath("td[17]//text()").get()
                skater['shot_percent'] = row.xpath("td[18]//text()").get()
                # Ice Time
                skater['toi'] = row.xpath("td[19]//text()").get()
                skater['atoi'] = row.xpath("td[20]//text()").get()
                # Misc
                skater['blk'] = row.xpath("td[24]//text()").get()
                skater['hit'] = row.xpath("td[25]//text()").get()
                skater['fow'] = row.xpath("td[26]//text()").get()
                skater['fol'] = row.xpath("td[27]//text()").get()
                skater['fo_percent'] = row.xpath("td[28]//text()").get()
            except IndexError as e:
                print(e)
            yield skater
