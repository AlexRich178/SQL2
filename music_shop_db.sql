
create table if not exists musical_genre(
	id serial primary key,
	name varchar(40) unique not null
);

create table if not exists artist(
	id serial primary key,
	name varchar(40) unique not null
);

create table if not exists GenreArtist(
	genre_id integer references musical_genre(id),
	artist_id integer references artist(id),
	constraint ga primary key(genre_id, artist_id)
);

create table if not exists album(
	id serial primary key,
	name varchar(40) unique not null,
	year integer not null
	
);

create table if not exists AlbumArtist(
	album_id integer references album (id),
	artist_id integer references artist(id),
	constraint aa primary key(album_id, artist_id)
);


create table if not exists track(
	id serial primary key,
	album_id integer not null references album(id),
	name varchar(40) unique not null,
	duration_sec integer not null
);

create table if not exists music_collection(
	id serial primary key,
	name varchar(40) not null,
	year integer not null
);

create table if not exists TrackCollection(
	track_id integer references track(id),
	collection_id integer references music_collection(id),
	constraint tc primary key(track_id, collection_id)
);



