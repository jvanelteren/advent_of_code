#%%
import database as db
conn = db.open_db('aoc.db')
sql = """
WITH year_scores AS (
    SELECT year, user, SUM(points) as total
    FROM scores
    GROUP BY 1,2
    ORDER BY 3 DESC),

'toppers' as (
    SELECT user
    FROM year_scores
    GROUP BY 1
    HAVING count(user) > 5),

'toppers_rank' as (
    SELECT user, year, total, ROUND(CAST(total as real)/SUM(total) OVER (
        PARTITION BY user
    ),2) as rank
    FROM year_scores
    WHERE user in toppers
    ORDER BY user, year)

SELECT t.year, AVG(t.rank), f.both, 25*(AVG(f2.both)*2+AVG(f2.first))
FROM toppers_rank as t
JOIN finishers f
ON f.year = t.year
JOIN finishers f2
ON f2.year = t.year
WHERE f.day = 1
GROUP BY t.year

"""
# -- SELECT * FROM scores LIMIT 5
res = db.do(conn, sql)

# %%
# %%
df = pd.DataFrame(res)
df.columns = ["year", "percentage_points", "num_starters", "num_stars"]

import altair as alt
from vega_datasets import data

source = df

alt.Chart(source).mark_point().encode(
    x='num_starters',
    y='percentage_points',
    tooltip='year'
)
# %%
alt.Chart(source).mark_point().encode(
    x='num_stars',
    y='percentage_points',
    tooltip='year'
)
# %%
alt.Chart(source).mark_point().encode(
    x='year:O',
    y='percentage_points'
)
# %%
df.corr()
# %%
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline

import numpy as np
arr = df.to_numpy()

#%%
pipe = make_pipeline(StandardScaler(), PCA(n_components=1))
pca_res = pipe.fit_transform(arr[:,1:])
df['pca'] = [p[0] for p in pca_res]
df
# conclusion, 2020 most competitive so far, 2016 least competitive
# %%

# This didn't really work, with the biases of the users

import pandas as pd
import pickle
import numpy as np
from fastai.collab import *
from pprint import pprint
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.neighbors import NearestNeighbors
import altair as alt
%matplotlib inline
import database as db
conn = db.open_db('scores.db')

sql = """
    SELECT year || '-' || day, year, day, user, time, points
    FROM scores
    WHERE star = 2
"""
# -- SELECT * FROM scores LIMIT 5
data = db.do(conn, sql)
df = pd.DataFrame(data)
df.columns=['puzzle', 'year', 'day', 'user', 'time', 'points']
df['time'] = df['time']**0.5
# %%

# %%
from fastai.collab import *
dls = CollabDataLoaders.from_df(df, 
    item_name='puzzle', 
    user_name = 'user',
    rating_name = 'time',
    bs=64)

learn = collab_learner(dls, n_factors=5, y_range=(0, 120))
learn.lr_find()

# %%
learn.fit_one_cycle(5, 0.06, wd=0.1)
# %%
# df.sort_values(['time'], ascending=False, inplace=True)
puz = df['puzzle'].unique()
movie_bias = learn.model.bias(puz, is_item=True)
movie_bias.shape
mean_ratings = df.groupby('puzzle')['time'].mean()
movie_ratings = [(b.item(), i, mean_ratings.loc[i]) for i,b in zip(puz,movie_bias)]
# %%

len(learn.model.bias(df['user'].unique(), is_item=False))

#%%
sql = """
    SELECT year || '-' || day, year, day, user, time, points
    FROM scores
"""
# -- SELECT * FROM scores LIMIT 5
data = db.do(conn, sql)
df = pd.DataFrame(data)
df.columns=['puzzle', 'year', 'day', 'user', 'time', 'points']

out = df.groupby(['year', 'user']).sum().reset_index()
out.sort_values(['year','points'], ascending=False, inplace=True)
# %%
out.head()
# %%
year = 2015
for year in range(2015, 2021):
    print(learn.model.bias(out[out['year'] == year]['user'][:100], is_item=False).mean())
# %%
learn.model.bias(out[out['year'] == 2020]['user'][:10], is_item=False)
# %%

# %%

# %%

# %%

# %%
