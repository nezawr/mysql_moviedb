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

''' api_request = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US" '''

movie_id = 1


for i in range(1,700):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US")
    data = response.json()
    #no matching movie_id
    if "success" in data:
        continue

    '''DATA'''
    #inserted into movies table
    movie_id            = data["movie_id"]
    title               = data["title"]
    adult               = data["adult"]
    budget              = data["budget"]
    imdb_id             = data["imdb_id"]
    overview            = data["overview"]
    original_language   = data["original_language"]
    popularity          = data["popularity"]
    release_data        = data["release_data"]
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


    ''' INSERTIONS
    notice sql insertion syntax: when inserting all columns, no need to
    list them. '''

    # movies table
    sqlmovies = "INSERT INTO movies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    movie_data = (movie_id, title, adult, budget, imdb_id, overview, original_language, popularity, release_data, revenue, status, vote_average, vote_count, video)

    cursor.execute(sqlmovies, movie_data)
    
    # genres, moviegenres tables
    sqlgenres      = "INSERT IGNORE INTO genres VALUES (%s, %s)"
    # here we need to specifiy columns, not all columns are used.
    sqlmoviegenres = "INSERT INTO moviegenres (movieid, genreid) VALUES (%s, %s) "
    for genre_id in genres:
        genre_data = (genre_id, genres[genre_id])
        moviegenre_data = (movie_id, genre_id)

        cursor.execute(sqlgenres, genre_data)
        cursor.execute(sqlmoviegenres, moviegenre_data)

    #production_companies, movieprodcomp tables
    sqlprodcomp = "INSERT IGNORE INTO production_companies VALUES (%s, %s)"
    sqlmovie_prodcomp = "INSERT INTO movieprodcomp (movieid, production_companyid) VALUE (%s, %s)"
    for prodcomp_id in production_companies:
        prodcomp_data =  (prodcomp_id, production_companies[prodcomp_id])
        movie_prodcomp_data = (movie_id, prodcomp_id)

        cursor.execute(sqlprodcomp, prodcomp_data)
        cursor.execute(sqlmovie_prodcomp, movie_prodcomp_data)

    #production_countries, movieprodcountry tables
    sqlprodcountry = "INSERT IGNORE INTO production_countries VALUES (%s, %s)"
    sqlmovie_prodcountry = "INSERT INTO movieprodcountry(movieid, production_countryid) VALUE (%s, %s)"
    for prodcountry_id in production_countries:
        prodcountry_data =  (prodcountry_id, production_countries[prodcountry_id])
        movie_prodcountry_data = (movie_id, prodcountry_id)

        cursor.execute(sqlprodcountry, prodcountry_data)
        cursor.execute(sqlmovie_prodcountry, movie_prodcountry_data)

    #spoken_languages, moviespokenlang tables
    sqlspoken_langauges = "INSERT IGNORE INTO spoken_languages VALUES (%s, %s)"
    sqlmovie_spoken_language = "INSERT INTO moviespokenlang (movieid, spoken_languageid) VALUE (%s, %s)"
    for spokenlang_id in spoken_languages:
        spokenlang_data =  (spokenlang_id, spoken_languages[spokenlang_id])
        moviespokenlang_data = (movie_id, spokenlang_id)

        cursor.execute(sqlspoken_langauges, spokenlang_data)
        cursor.execute(sqlmovie_spoken_language, moviespokenlang_data)

    



    






    cnx.commit()

    
    #insert into spoken_languages
    spoken_languages = data["spoken_languages"]




cnx.close()