#%%
import numpy as np
import altair as alt
import pandas as pd

f= open('scores.txt','r')
scores = [line.rstrip().split(',') for line in f]
f= open('scores_leaderboard.txt','r')
leaderboard_scores = [line.rstrip().split(',') for line in f]

#total puzzle time is field 2
x = np.array([int(s[2]) for s in scores])
y = np.array([int(s[2]) for s in leaderboard_scores])

source = pd.DataFrame({'personal':x,'leaderboard':y,'label':list(range(1,26))})
points = alt.Chart(source).mark_point().encode(
    x=alt.X('personal:Q',scale=alt.Scale(domain=(0, 200))),
    y=alt.Y('leaderboard:Q',scale=alt.Scale(domain=(0,60)))
)
text = points.mark_text(
    align='left',
    baseline='middle',
    dx=7
).encode(
    text='label'
)
points + text
# %%
# scrape AoC for leaderboard information
import requests
import time
import re
import datetime
def getfile(year,day):
    url = 'https://adventofcode.com/'+str(year)+'/leaderboard/day/'+str(day)
    r = requests.get(url)
    time.sleep(1)
    print(day)
    return r.text
year = 2016
highscores = [getfile(year,day) for day in range(1,26)]
#%%
# make file after scraping
with open('scores_leaderboard.txt','w') as f:
    for day,times in enumerate(highscores):
        times = re.findall(r'leaderboard-position">100\)</span> <span class="leaderboard-time">Dec ..  (.*?)</span>',times)
        times = [t.split(':') for t in times]
        times = [datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(t[2])) for t in times]
        times = [f'{t.total_seconds()/60:.0f}' for t in times]
        f.write(f'{day+1},{int(times[1])},{int(times[0])}\n')



# %%
