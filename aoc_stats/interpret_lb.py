#%% 
%load_ext autoreload
%autoreload 2
import pandas as pd
import database as db
import sqlite3
from pprint import pprint

conn = db.open_db('scores.db')


sql = """
    SELECT user, SUM(points) 
    FROM scores 
    -- WHERE SUM(points) > 1000
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
"""
db.do_df(conn,sql)




# %%
sql = """
    SELECT DISTINCT year
    FROM finishers
    LIMIT 10
"""
scores = db.do_df(conn,sql)
scores.head()
# %%

# %%

# %%

#%%
sql = """
    SELECT f1.year, f1.day, 
        ROUND(CAST(f1.both as real) / f2.both, 2) AS perc_of_previous, 
        ROUND(CAST(f1.both as real) / (f1.both+f1.first), 2) AS perc_both_stars,
        MIN(s.time)/60, SUM(s.time)/100/60
    
    FROM finishers f1
    JOIN finishers f2
    ON f2.year = f1.year AND (f1.day - f2.day = 1)
    JOIN scores s
    ON s.year = f1.year and s.day = f1.day and s.star=2
    GROUP BY 1,2
    ORDER BY 3

    LIMIT 10
    
"""
# -- SELECT * FROM scores LIMIT 5
pprint(db.do(conn, sql))

# %%
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

# %%
sql = """
    SELECT year || '-' || day || '-' || star, user, time
    FROM scores
"""
# -- SELECT * FROM scores LIMIT 5
data = db.do(conn, sql)
df = pd.DataFrame(data)
df.columns=['puzzle', 'user', 'time']
df['time'] = df['time']**0.5
# %%
import pandas as pd
import pickle
import numpy as np
from fastai.collab import *
from pprint import pprint
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.neighbors import NearestNeighbors
%matplotlib inline
# %%
from fastai.collab import *
dls = CollabDataLoaders.from_df(df, 
    item_name='puzzle', 
    user_name = 'user',
    rating_name = 'time',
    bs=64)
# %%
learn = collab_learner(dls, n_factors=30, y_range=(0, 120))
learn.fit_one_cycle(5, 5e-3, wd=0.1)
# %%
df.sort_values(['time'], ascending=False, inplace=True)
puz = df['puzzle'].unique()
movie_bias = learn.model.bias(puz, is_item=True)
movie_bias.shape
mean_ratings = df.groupby('puzzle')['time'].mean()
movie_ratings = [(b.item(), i, mean_ratings.loc[i]) for i,b in zip(puz,movie_bias)]
# %%
item0 = lambda o:o[0]
most_difficult = pd.DataFrame(sorted(movie_ratings, key=item0, reverse=True))
most_difficult.columns= ['bias','puzzle', 'time']
# most_difficult['bias'] = list(map(most_difficult['bias'], lambda x: x.item))
most_difficult['year'] = most_difficult['puzzle'].str[:4]

# %%

alt.Chart(most_difficult.loc[(most_difficult['time']<60) * (most_difficult['bias']<0)]).mark_point().encode(
    x='time',
    y='bias',
    tooltip = 'puzzle',
    color = 'year'
)
# %%
from sklearn import linear_model
for i in range(2015, 2021):
    temp = most_difficult[most_difficult['year']== str(i)]
    reg = linear_model.LinearRegression().fit(temp[['time']], temp['bias'])
    print(reg.coef_,reg.intercept_, reg.score(temp[['time']], temp['bias']))
# %%

# %%
movie_w = learn.model.weight(puz, is_item=True)
movie_pca = movie_w.pca(3)
fac0,fac1,fac2 = movie_pca.t()
idxs = np.random.choice(len(puz), len(puz), replace=False)
idxs = list(range(len(puz)))
X = fac0[idxs]
Y = fac1[idxs]
plt.figure(figsize=(15,15))
plt.scatter(X, Y)
for i, x, y in zip(puz[idxs], X, Y):
    plt.text(x,y,i, color=np.random.rand(3)*0.7, fontsize=11)
plt.show()
# %%
movie_w
# %%

# %%
