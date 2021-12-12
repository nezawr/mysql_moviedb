import requests
import json
import mysql.connector 

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

movie_id = 8

response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US")

data = response.json()


title               = data["title"]
adult               = data["adult"]
budget              = data["budget"]
imdb_id             = data["imdb_id"]
overview            = data["overview"]
original_language   = data["original_language"]
popularity          = data["popularity"]
release_date        = data["release_date"]
revenue             = data["revenue"]
status              = data["status"]
vote_average        = data["vote_average"]
vote_count          = data["vote_count"]
video               = data["video"]
#insert into genres
genres = data["genres"]
#insert into production_companies
production_companies = data["production_companies"]
#insert into production_countries
production_countries = data["production_countries"]
#insert into spoken_languages
spoken_languages = data["spoken_languages"]

sqlmovies = "INSERT INTO movies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
movie_data = (movie_id, title, adult, budget, imdb_id, overview, original_language, popularity, release_date, revenue, status, vote_average, vote_count, video)

cursor.execute(sqlmovies, movie_data)

# genres, moviegenres tables, IGNORE if it's already in table.
sqlgenres      = "INSERT IGNORE INTO genres VALUES (%s, %s)"
# here we need to specifiy columns, not all columns are used.
sqlmoviegenres = "INSERT INTO moviegenres (movie_id, genre_id) VALUES (%s, %s) "
for genre in genres:
    genre_data = (genre["id"], genre["name"])
    moviegenre_data = (movie_id, genre["id"])

    cursor.execute(sqlgenres, genre_data)
    cursor.execute(sqlmoviegenres, moviegenre_data)

cnx.commit()


cnx.close()