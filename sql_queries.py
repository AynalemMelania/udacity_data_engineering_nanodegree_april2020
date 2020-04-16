""" 
This file contains sql_queries used in project:
    DROP TABLES
    CREATE TABLES
    INSERT RECORDS
    FIND SONGS
    QUERY LISTS
"""
# DROP TABLES
songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES
songplay_table_create = ("""create table songplays(
songplay_id serial primary key,
start_time bigint not null,
user_id int not null,
level text,
song_id text not null,
artist_id text not null,
session_id int,
location text,
user_agent text);
""")

user_table_create = ("""create table users(
user_id int primary key, 
first_name text,
last_name text, 
gender char(1), 
level text);
""")

song_table_create = ("""create table songs(
song_id text primary key, 
title text, 
artist_id text not null,
year int, 
duration float);
""")

artist_table_create = ("""create table artists(
artist_id text primary key, 
name text, 
location text, 
latitude numeric, 
longitude numeric);
""")

time_table_create = ("""create table time(
start_time timestamp primary key, 
hour int, 
day int,
week int,
month int, 
year int, 
weekday int);
""")

# INSERT RECORDS
songplay_table_insert = ("""insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) 
values( %s, %s, %s, %s, %s) on conflict(user_id) do update set level = excluded.level
""")

song_table_insert = (""" insert into songs(song_id, title, artist_id, year, duration) 
values(%s, %s, %s, %s, %s) on conflict(song_id) do update set duration = excluded.duration
""")

artist_table_insert = ("""insert into artists(artist_id, name, location, latitude, longitude) 
values(%s, %s, %s, %s, %s) on conflict(artist_id) do update set latitude = excluded.latitude
""")

time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday) 
values(%s, %s, %s, %s, %s, %s, %s) on conflict(start_time) do update set weekday = excluded.weekday
""")
 
# FIND SONGS

song_select = ("""select s.song_id, s.artist_id from songs s
join artists a 
on s.artist_id=a.artist_id
where s.title = %s and a.name=%s and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]