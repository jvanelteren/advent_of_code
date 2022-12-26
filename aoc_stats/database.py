#%%
import sqlite3
from sqlite3 import Error
import pandas as pd

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
    sql = """ INSERT OR IGNORE INTO scores (year, day, star, position, points, time, user, aocplus)
              VALUES(?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.executemany(sql,scores)
    print(f'{cur.rowcount} items inserted')
    conn.commit()

def insert_personal_scores(conn, scores):
    sql = """ INSERT OR IGNORE INTO personal (year, day, star, position, time)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.executemany(sql,scores)
    print(f'{cur.rowcount} items inserted')
    conn.commit()

def insert_finishers(conn, finishers):
    sql = """ INSERT INTO finishers (year, day, first, both)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.executemany(sql,finishers)
    print(f'{cur.rowcount} items inserted')
    conn.commit()

def del_all_records(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS scores")
    cur.execute("DROP TABLE IF EXISTS finishers")
    cur.execute("DROP TABLE IF EXISTS personal")
    conn.commit()

def len(conn, table):
    return do(conn, f"SELECT COUNT(*) FROM {table}")

def first(conn, table):
    return do(conn, f"SELECT * FROM {table} LIMIT 5")



def open_db(name):
    sql_create_table_scores = """ CREATE TABLE IF NOT EXISTS "scores"(
                                        "id" INTEGER PRIMARY KEY,
                                        "year" INTEGER,
                                        "day" INTEGER,
                                        "star" INTEGER,
                                        "position" INTEGER,
                                        "points" INTEGER,
                                        "time" INTEGER,
                                        "user" VARCHAR(100),
                                        "aocplus" VARCHAR(100),
                                        UNIQUE(year, day, star, position)
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

    sql_create_table_personal = """ CREATE TABLE IF NOT EXISTS "personal"(
                                        "id" INTEGER PRIMARY KEY,
                                        "year" INTEGER,
                                        "day" INTEGER,
                                        "star" INTEGER,
                                        "position" INTEGER,
                                        "time" INTEGER,
                                        UNIQUE(year, day, star)
                                        );
                                 """

    conn = create_con(name)

    if conn:
        create_table(conn, sql_create_table_scores)
        create_table(conn, sql_create_table_finishers)
        create_table(conn, sql_create_table_personal)
    return conn

def do(conn, ins):
    cur =  conn.cursor()
    res = cur.execute(ins).fetchall()
    cur.close()
    return res

def do_special(conn, ins):
    cur = conn.cursor()
    cur.execute(ins)
    conn.commit()
    cur.close()
    
def do_df(conn, ins):
    cur = conn.cursor().execute(ins)
    col_name_list = [tuple[0] for tuple in cur.description]
    res = pd.DataFrame(cur.fetchall(), columns=col_name_list)
    cur.close()
    return res

#%%
conn = open_db('aoc.db')
# #%%
print(first(conn, 'personal'))
# del_all_records(conn)


# # #%%
# # do(conn, "SELECT * FROM scores")
# # # %%

# # do(conn, "INSERT INTO scores (user) VALUES ('test')")
# # # %%

# # %%
# do(conn, "SELECT COUNT(*) FROM (SELECT DISTINCT year, day, star, position FROM scores)")
# # %%
# res = do(conn, "SELECT DISTINCT * FROM scores")

# #%%
# res[-1]
# # %%
