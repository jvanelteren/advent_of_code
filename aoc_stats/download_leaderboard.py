# %%
# scrape AoC for leaderboard information
import requests
import time
import re
from bs4 import BeautifulSoup
%load_ext autoreload
%autoreload 2
import database as db

# This file scrapes the website for the leaderboard times
# It's not necessary to run it <2020, since these files are already included
# Make sure to run this file only once, it will take about the minute (waits 2 seconds between requests)

# to add lb scores to db
def getfile(YEAR,day):
    url = 'https://adventofcode.com/'+str(YEAR)+'/leaderboard/day/'+str(day)
    r = requests.get(url)
    time.sleep(2)
    print(f'downloaded {YEAR} day {day}')
    return r.content.decode('utf-8')

def parse(year, day, webpage):
    soup = BeautifulSoup(webpage, 'html.parser')
    star = 2
    leaderboard = []
    for part in soup.find_all('div', attrs={'class': 'leaderboard-entry'}):
        res = []
        res = [p.string for p in part.descendants
                    if p.string and p.string not in ['None',' ']]
        place = int(res[0][:-1])
        timestamp = re.findall(r'(\d\d)',res[2])
        timestamp = int(timestamp[1])*3600 + int(timestamp[2])*60 + int(timestamp[3])
        user = res[4]
        aocplus = True if '(AoC++)' in res else False
        leaderboard.append((year, day, star, place, timestamp, user, aocplus))
        if place == 100: star = 1
    return leaderboard

conn = db.open_db('scores.db')
# YEAR = 2015 # adapt to the year you're competing
for YEAR in list(range(2015,2021)):
    highscores = [getfile(YEAR,day) for day in range(1,26)]
    for day, scores in enumerate(highscores):
        db.insert_scores(conn, parse(YEAR, day + 1, scores))
        print(db.do(conn, "SELECT COUNT(*) FROM scores"))

# %%
# to add the stats to the DB
def getstats(YEAR):
    url = 'https://adventofcode.com/'+str(YEAR)+'/stats'
    r = requests.get(url)
    time.sleep(2)
    print(f'downloaded {YEAR}')
    return r.content.decode('utf-8')

conn = db.open_db('scores.db')

for YEAR in list(range(2015,2021)):
    test = getstats(YEAR)
    soup = BeautifulSoup(test, 'html.parser')
    both = soup.find_all('span', attrs={'class': 'stats-both'})
    first = soup.find_all('span', attrs={'class': 'stats-firstonly'})

    res = []
    for i in range(len(both)):
        try:
            res.append((YEAR, 25-len(res), int(first[i].string), int(both[i].string)))
        except Exception:
            pass

    db.insert_finishers(conn, res)
    print(db.do(conn, "SELECT COUNT(*) FROM finishers"))
#%%
