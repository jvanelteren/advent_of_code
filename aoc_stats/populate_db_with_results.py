# %%
# scrape AoC for leaderboard information
import requests
import time
import re
from bs4 import BeautifulSoup
# %load_ext autoreload
# %autoreload 2
import database as db
from pathlib import Path

# This file scrapes the website for the leaderboard times
# It's not necessary to run it <2022, since these files are already included
# Make sure to run this file only once, it will take about the minute (waits 2 seconds between requests)
HEADERS = {
    "User-Agent": (
        f"https://github.com/jvanelteren/advent_of_code/tree/main/aoc_stats"
        " contact: Reddit u/asgardian28 Thanks for AoC Eric. Im scraping this once per year"
    )
}
# to add lb scores to db
def getfile(YEAR,day):
    url = 'https://adventofcode.com/'+str(YEAR)+'/leaderboard/day/'+str(day)
    r = requests.get(url, headers=HEADERS)
    
    
    
    time.sleep(2)
    print(f'downloaded {YEAR} day {day}')
    return r.content.decode('utf-8')

def parse(year, day, webpage):
    soup = BeautifulSoup(webpage, 'html.parser')
    star = 2
    leaderboard = []
    for part in soup.find_all('div', class_='leaderboard-entry'):
        res = [p.text for p in part.descendants
                    if p.text and p.text not in ['None',' ']]
        place = int(res[0][:-1])
        points = 100 - place + 1
        timestamp = re.findall(r'(\d\d)',res[2])
        timestamp = int(timestamp[1])*3600 + int(timestamp[2])*60 + int(timestamp[3])
        user = res[4]
        aocplus = True if '(AoC++)' in res else False
        leaderboard.append((year, day, star, place, points, timestamp, user, aocplus))
        if place == 100: star = 1
    return leaderboard

YEAR = 2023 # adapt to the year you're competing
def add_daily_lb_to_db(year, conn):
    for day in range(1,26):
        scores = getfile(year,day)
        db.insert_scores(conn, parse(year, day, scores))
# %%
# to add the stats to the DB
def getstats(YEAR):
    url = 'https://adventofcode.com/'+str(YEAR)+'/stats'
    r = requests.get(url)
    time.sleep(2)
    print(f'downloaded {YEAR}')
    return r.content.decode('utf-8')

def extract_int_from_soup_findall(soup_findall):
    # bs returns all hits, but sometimes we are only interested in the integers
    return [int(tag.text) for tag in soup_findall if re.search(r'\d+', tag.text)]

    
def add_year_stats_to_db(year, conn):
    page = getstats(year)
    soup = BeautifulSoup(page, 'html.parser')
    bothtags = soup.find_all('span', class_='stats-both')
    firsttags = soup.find_all('span', class_='stats-firstonly')
    both = extract_int_from_soup_findall(bothtags)
    first = extract_int_from_soup_findall(firsttags)
    res = [(year, 25-day, f, b) for day, (f, b) in enumerate(zip(first, both))]
    db.insert_finishers(conn, res)
    print(db.do(conn, "SELECT COUNT(*) FROM finishers"))

def timestamp2int(timestamp):
    timestamp = list(map(int, timestamp.split(':')))
    return timestamp[0] * 3600 + timestamp[1] * 60 + timestamp[2]

def parse_times_incl_position(content, year):
    scores = []
    lines = [line.split() for line in content.splitlines()]
    for line in lines:
        if len(line) == 7 and line[0] != 'Day':
            day, timestamp1, place1, score1, timestamp2, place2, score2 = line
            scores.append((year, day, 1, place1, timestamp2int(timestamp1)))
            scores.append((year, day, 2, place2, timestamp2int(timestamp2)))
    print(scores, year)
    return scores

def parse_times_excl_position(content, year):
    lines = content.splitlines()
    scores = []
    for line in lines:
        day, time1, time2 = line.split(',')
        scores.append((year, day, 1, None, int(time1) * 60))
        scores.append((year, day, 2, None, int(time2) * 60))
    return scores

def parse_personal_scores(conn):
    for x in Path('personal_scores').iterdir():
        with open(x, 'r') as f:
            content = f.read()
            year = int(x.name[19:-4])
            if '-------Part 1--------' in content:
                print(year)
                # competed this year for position, aoc website page such as:
                # https://adventofcode.com/2021/leaderboard/self
                scores = parse_times_incl_position(content, year)
            else:
                # didnt compete for position but for time. Format:
                # day, timepart1, timepart1and2
                scores = parse_times_excl_position(content, year)
            db.insert_personal_scores(conn, scores)
                

# this drops the personal scores and reloads them from text files
conn = db.open_db('aoc.db')
db.do(conn, "DROP TABLE IF EXISTS personal")
db.do(conn, "DROP TABLE IF EXISTS finishers")
conn = db.open_db('aoc.db')
parse_personal_scores(conn)

# enter a year if you need to add new global scores to db
# scrape_years = [2023]
scrape_years = range(2015, 2025)
for y in scrape_years:
    # add_daily_lb_to_db(y, conn)
    print(f'items in db after adding year {y}:', db.len(conn, 'scores'))
    add_year_stats_to_db(y, conn)
    print(f'items in db after adding year {y}:', db.len(conn, 'finishers'))

conn = db.open_db('aoc.db')
print(db.len(conn, 'scores'), db.len(conn, 'finishers'), db.len(conn, 'personal'))
# %%
