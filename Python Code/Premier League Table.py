import requests
from bs4 import BeautifulSoup

premier_league_url = 'https://www.skysports.com/premier-league-table'

request = requests.get(premier_league_url)
website_scrapping = BeautifulSoup(request.text,'html.parser')
league_table = website_scrapping.find('table', class_ = 'standing-table__table callfn')

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        position = row.find('td',class_ ='standing-table__cell').text
        team = row.find('td',class_ ="standing-table__cell standing-table__cell--name").text.rstrip()
        points = row.find_all ('td',class_ ="standing-table__cell")[9].text
        print(f"{team} are {position} with {points} points")
