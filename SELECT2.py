import sqlalchemy

db = 'postgresql://alex:1619@localhost:5432/test1'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# 1 количество исполнителей в каждом жанре
artist_count = connection.execute(
    """SELECT name, COUNT(*) FROM genreartist ga
        LEFT JOIN musical_genre mg ON mg.id = ga.genre_id
        GROUP BY name
        ORDER BY COUNT(*);
    """
).fetchall()
print(artist_count)

# 2 количество треков, вошедших в альбомы 2019-2020 годов
track_album = connection.execute(
    """SELECT COUNT(t.id) FROM track t
        LEFT JOIN album a ON a.id = t.album_id
        WHERE year BETWEEN 2019 AND 2020;
    """
).fetchall()
print(track_album)

# 3 средняя продолжительность треков по каждому альбому
track_duration = connection.execute(
    """SELECT a.name, round(AVG(duration_sec),1) FROM track t
        LEFT JOIN album a ON a.id = t.album_id
        GROUP BY a.name;
    """
).fetchall()
print(track_duration)

# 4 все исполнители, которые не выпустили альбомы в 2020 году
not_artist = connection.execute(
    """SELECT ar.name, al.year FROM albumartist aa
        LEFT JOIN artist ar ON ar.id = aa.artist_id
        LEFT JOIN album al ON al.id = aa.album_id
        WHERE ar.name NOT IN (SELECT ar.name FROM albumartist
                                WHERE al.year = 2020);
    """
).fetchall()
print(not_artist)

# 5 названия сборников, в которых присутствует конкретный исполнитель (Rammstein)
collection = connection.execute(
    """SELECT DISTINCT mc.name FROM trackcollection tc
        LEFT JOIN track t ON t.id = tc.track_id
        LEFT JOIN albumartist aa ON aa.album_id = t.album_id
        LEFT JOIN artist ar ON ar.id = aa.artist_id
        LEFT JOIN music_collection mc ON mc.id = tc.collection_id
        WHERE ar.name = 'Rammstein';
    """
).fetchall()
print(collection)

# 6 название альбомов, в которых присутствуют исполнители более 1 жанра
album_genre = connection.execute(
    """SELECT a.name FROM album a
        LEFT JOIN albumartist aa ON aa.album_id = a.id
        LEFT JOIN artist ar ON ar.id = aa.artist_id 
        LEFT JOIN genreartist ga ON ga.artist_id = ar.id
        LEFT JOIN musical_genre mg ON mg.id = ga.genre_id
        GROUP BY a.name
        HAVING COUNT(a.name) > 1;
    """
).fetchall()
print(album_genre)

# 7 наименование треков, которые не входят в сборники
track_collection = connection.execute(
    """SELECT t.name FROM track t
        LEFT JOIN trackcollection tc ON tc.track_id = t.id
        LEFT JOIN music_collection mc ON mc.id = tc.collection_id
        WHERE mc.name IS NULL;
    """
).fetchall()
print(track_collection)

# 8 исполнителя(-ей), написавшего самый короткий по продолжительности трек
low_dur = connection.execute(
    """SELECT ar.name FROM track t
        LEFT JOIN albumartist aa ON aa.album_id = t.album_id
        LEFT JOIN artist ar ON ar.id = aa.artist_id
        WHERE t.duration_sec = (SELECT MIN(duration_sec) FROM track);
    """
).fetchall()
print(low_dur)

# 9 название альбомов, содержащих наименьшее количество треков
album_name = connection.execute(
    """SELECT a.name FROM track t
        LEFT JOIN album a ON a.id = t.album_id
        GROUP BY a.name
        HAVING COUNT(t.name) = (SELECT COUNT(t.name) FROM track t
                                LEFT JOIN album a ON a.id = t.album_id
                                GROUP BY a.name
                                ORDER BY COUNT(t.name)
                                LIMIT 1);
    """
).fetchall()
print(album_name)

