# %%

import numpy as np
import altair as alt
import pandas as pd

# The display part needs two files: scores_leaderboard_YEAR.txt and scores_personal_YEAR.txt which you need to make yourself
YEAR = 2020 # adapt to the year you're competing

f= open('personal_scores/scores_personal_'+str(YEAR)+'.txt','r')
scores = [line.rstrip().split(',') for line in f]
f= open('global_scores/scores_leaderboard_'+str(YEAR)+'.txt','r')
leaderboard_scores = [line.rstrip().split(',') for line in f]

# first puzzle time is field 1
x = np.array([int(s[1]) for s in scores])
y = np.array([int(s[1]) for s in leaderboard_scores])

source = pd.DataFrame({'personal':x,'leaderboard':y,'label':list(range(1,26))})
points_star1 = alt.Chart(source).mark_point().encode(
    x=alt.X('personal:Q',scale=alt.Scale(domain=(0, 200))),
    y=alt.Y('leaderboard:Q',scale=alt.Scale(domain=(0,60)))
).properties(
    title='Performance on first star '+str(YEAR),
    width=600,
    height=600)

text_star1 = points_star1.mark_text(
    align='left',
    baseline='middle',
    dx=7
).encode(
    text='label'
)

# total puzzle time is field 2
x = np.array([int(s[2]) for s in scores])
y = np.array([int(s[2]) for s in leaderboard_scores])

source = pd.DataFrame({'personal':x,'leaderboard':y,'label':list(range(1,26))})
points_star2 = alt.Chart(source).mark_point().encode(
    x=alt.X('personal:Q',scale=alt.Scale(domain=(0, 200))),
    y=alt.Y('leaderboard:Q',scale=alt.Scale(domain=(0,60)))
).properties(
    title='Performance on both stars '+str(YEAR),
    width=600,
    height=600)

text_star2 = points_star2.mark_text(
    align='left',
    baseline='middle',
    dx=7
).encode(
    text='label'
)
((points_star1 + text_star1) | (points_star2 + text_star2)).save('chart_'+str(YEAR)+'.html')


# %%
