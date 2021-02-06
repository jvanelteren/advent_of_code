#%%
import sqlite3
from sqlite3 import Error

def create_con(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def insert_scores(conn, scores):
    sql = """ INSERT INTO scores (year, day, star, position, time, user, aocplus)
              VALUES(?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.executemany(sql,scores)
    conn.commit()
    return cur.lastrowid

def insert_finishers(conn, finishers):
    sql = """ INSERT INTO finishers (year, day, first, both)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.executemany(sql,finishers)
    conn.commit()
    return cur.lastrowid

def del_all_records(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS predictions")
    conn.commit()


from sqlalchemy import create_engine

def open_db(name):
    sql_create_table_scores = """ CREATE TABLE IF NOT EXISTS "scores"(
                                        "id" INTEGER PRIMARY KEY,
                                        "year" INTEGER,
                                        "day" INTEGER,
                                        "star" INTEGER,
                                        "position" INTEGER,
                                        "time" INTEGER,
                                        "user" VARCHAR(100),
                                        "aocplus" VARCHAR(100)
                                        );
                                        """

    sql_create_table_finishers = """ CREATE TABLE IF NOT EXISTS "finishers"(
                                        "id" INTEGER PRIMARY KEY,
                                        "year" INTEGER,
                                        "day" INTEGER,
                                        "first" INTEGER,
                                        "both" INTEGER
                                        );
                                 """

    conn = create_con(name)

    if conn:
        # engine = create_engine('sqlite:///%s' % 'hi.db', echo=True)
        # c = conn.cursor()
        # c.execute(""" DROP TABLE IF EXISTS games""")
        # create_table(conn, sql_create_table_games)
        # c.execute(""" DROP TABLE IF EXISTS predictions""")
        create_table(conn, sql_create_table_scores)
        create_table(conn, sql_create_table_finishers)

        
    return conn

def open_upload(name):
    sql_create_table_uploads = """ CREATE TABLE IF NOT EXISTS uploads(
                                        id integer PRIMARY KEY,
                                        date text NOT NULL
                                        )
                                    """

    conn2 = create_con(name)

    if conn2:
        # engine = create_engine('sqlite:///%s' % 'hi.db', echo=True)
        # c = conn.cursor()
        # c.execute(""" DROP TABLE IF EXISTS games""")
        # create_table(conn, sql_create_table_games)
        # c.execute(""" DROP TABLE IF EXISTS predictions""")
        create_table(conn2, sql_create_table_uploads)
        
    return conn2
import pandas as pd
def do(conn, ins):
    return conn.cursor().execute(ins).fetchall()

def do_df(conn, ins):
    cur = conn.cursor().execute(ins)
    col_name_list = [tuple[0] for tuple in cur.description]
    return pd.DataFrame(cur.fetchall(), columns=col_name_list)

#%%
# conn = open_db('scores.db')
# # conn = open_db('predictions.db')
# # c = count_predictions(conn)
# del_all_records(conn)
# # c

# #%%
# do(conn, "SELECT * FROM scores")
# # %%

# do(conn, "INSERT INTO scores (user) VALUES ('test')")
# # %%

# %%
