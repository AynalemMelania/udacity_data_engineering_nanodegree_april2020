# Project Spartkify with PostgreSQL

## About
Spartkify startup is a project of an app and a database with details about songs and users activities.
A data engineer could analyse on this type of data the behaviour of users, the most listened songs, artists' work
(for example how many songs they have in a year).

## Project Datasets
There are 2 resourses of data: log_data and song_data. They contain json files individualy. 
After manipulating the data, there would appear the logical relationships between users, artists and songs.

## Programming language
Python was chosen because it has many modules for manipulating the data. 
Here, pandas was used to process different types of files and a pandas object can storage multidimensional arrays.

## Example
```json
{num_songs:1
artist_id:"ARIK43K1187B9AE54C"
artist_latitude:null
artist_longitude:null
artist_location:"Beverly Hills, CA"
artist_name:"Lionel Richie"
song_id:"SOBONFF12A6D4F84D8"
title:"Tonight Will Be Alright"
duration:307.3824
year:1986}
``` 

```python
filepath = '/home/workspace/data/song_data/A/B/C/TRABCRU128F423F449.json'
df = pd.read_json(filepath, lines=True) 
```

## DataBase
PostgreSQL keeps the tables with details for 5 tables on a star schema.
Songplays table is the center of the tables.
The main relationships are Many to Many:
A user can listen more songs. A song can be listened by more users.

## Tables from database
- table songplays:
songplay_id| start_time| user_id| artist_id| session_id| location| user_agent
- table song
song_id| artist_id| year| duration
- table artists:
artist_id| name| location| latitude| longitude
- table users:
user_id| first_name| last_name| gender| level
- table time:
star_time| hour| day| week| month| year| weekday

## Python files
- .ipynb test only a single json file and shows the result at every instruction
- .py test on multiples json files shows the result of the all database

## Builded ETL Processes 
ETL process takes data from json files, extracts and transform the information into pandas objects 
as multidimensional tables with different types of properties, after loads it to the database. 

## Testing Terminal
- python3 sql_queries.py
- python3 create_tables.py
- pytho3 etl.py
 
## Testing Jupyter Notebook
Run Cells:
- etl.ipynb shows every cell return
- test.ipynb shows several selects from tables
