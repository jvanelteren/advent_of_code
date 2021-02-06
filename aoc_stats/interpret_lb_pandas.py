#%% 
%load_ext autoreload
%autoreload 2
import pandas as pd
import database as db
import pickle
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.neighbors import NearestNeighbors
import altair as alt
from fastai.collab import *
%matplotlib inline
# %%

conn = db.open_db('scores.db')

sql = """
    SELECT *
    FROM scores
"""
scores = db.do_df(conn,sql)
scores.head()
# %%
sql = """
    SELECT *
    FROM finishers
"""
finish = db.do_df(conn,sql)
finish.head()
# %%
difficulty = scores.loc[scores['star']==2].groupby(['year', 'day']).mean()['time'].reset_index()
difficulty = pd.merge(difficulty, (scores.loc[(scores['position'] == 1) & 
                            (scores['star']==2)])[['year', 'day', 'time']], 
                            on=['year','day'])
difficulty.rename(columns={'time_x':'fastest_time', 'time_y':'avg_time'}, inplace=True)

# %%
temp = finish.copy()
temp['day'] = temp['day']+1
finish = pd.merge(finish, temp[['year', 'day', 'both']], on = ['year', 'day'], how = 'left')


# %%
finish.rename(columns={'both_x':'both', 'both_y':'both_previous'}, inplace=True)
finish['perc_stuck_first'] = finish['first']  / (finish['first'] + finish['both'])
finish['completion_vs_prev_day'] = finish['both'] / finish['both_previous']

difficulty = pd.merge(difficulty, finish[['year', 'day', 'perc_stuck_first', 'completion_vs_prev_day']])
difficulty
#%%

# %%

# %%
sql = """
    SELECT year || '-' || day, year, day, user, time
    FROM scores
    WHERE star = 2
"""
# -- SELECT * FROM scores LIMIT 5
data = db.do(conn, sql)
df = pd.DataFrame(data)
df.columns=['puzzle', 'year', 'day', 'user', 'time']
df['time'] = df['time']**0.5
# %%

dls = CollabDataLoaders.from_df(df, 
    item_name='puzzle', 
    user_name = 'user',
    rating_name = 'time',
    bs=64)
# %%
learn = collab_learner(dls, n_factors=50, y_range=(0, 120))
learn.lr_find()

# %%
learn.fit_one_cycle(5, 0.03, wd=0.1)
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
difficulty['bias'] = [b.item() for b in movie_bias]
difficulty.fillna(value = 1, inplace=True)
arr = difficulty.to_numpy()
# %%

# %%
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(StandardScaler(), PCA(n_components=1))
pca_res = pipe.fit_transform(arr[:,2:])
difficulty['pca'] = [p[0] for p in pca_res]
# %%
pipe.named_steps['pca'].explained_variance_ratio_

difficulty.sort_values('pca', ascending=False)
# %%
output = difficulty.groupby('year').median().reset_index()
# %%
import altair as alt

alt.Chart(difficulty).mark_point().encode(
    x='year:O',
    y='avg_time',
    tooltip='year'
)

alt.Chart(difficulty).mark_point().encode(
    x='year:O',
    y='bias',
    tooltip='day'
)
output.corr()
# %%
