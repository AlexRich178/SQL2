import sqlalchemy

db = 'postgresql://alex:1619@localhost:5432/test1'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

year_2018 = connection.execute(
    """SELECT name, year FROM album
        WHERE year = 2018"""
).fetchall()
print(year_2018)

max_dur = connection.execute(
    """SELECT name, duration_sec FROM track
        WHERE duration_sec = (SELECT MAX(duration_sec) FROM track)"""
).fetchall()
print(max_dur)

dur = connection.execute(
    """SELECT name, duration_sec FROM track
        WHERE duration_sec >= 210"""
).fetchall()
print(dur)

between = connection.execute(
    """SELECT name FROM music_collection
        WHERE year BETWEEN 2018 AND 2020"""
).fetchall()
print(between)

one_word = connection.execute(
    """SELECT name FROM artist
        WHERE name NOT LIKE '%% %%'"""
).fetchall()
print(one_word)

track_name = connection.execute(
    """SELECT name FROM track
        WHERE name ILIKE '%%моя%%'"""
).fetchall()
print(track_name)
