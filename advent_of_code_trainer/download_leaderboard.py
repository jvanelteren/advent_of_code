# %%
# scrape AoC for leaderboard information
import requests
import time
import re
import datetime

# This file scrapes the website for the leaderboard times
# It's not necessary to run it <2020, since these files are already included
# Make sure to run this file only once, it will take about the minute (waits 2 seconds between requests)

YEAR = 2020 # adapt to the year you're competing


def getfile(YEAR,day):
    url = 'https://adventofcode.com/'+str(YEAR)+'/leaderboard/day/'+str(day)
    r = requests.get(url)
    time.sleep(2)
    print(f'downloaded {YEAR} day {day}')
    return r.text

highscores = [getfile(YEAR,day) for day in range(1,26)]

with open('global_scores/scores_leaderboard_'+str(YEAR)+'.txt','w') as f:
    for day,times in enumerate(highscores):
        try:
            times = re.findall(r'leaderboard-position">100\)</span> <span class="leaderboard-time">Dec ..  (.*?)</span>',times)
            times = [t.split(':') for t in times]
            times = [datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(t[2])) for t in times]
            times = [f'{t.total_seconds()/60:.0f}' for t in times]
            f.write(f'{day+1},{int(times[1])},{int(times[0])}\n')
        except Exception:
            print('Probably you are running the script on the current year and not all days are done yet',
                    'Please wait untill all days are finished')
# %%
