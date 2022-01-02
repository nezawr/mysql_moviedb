import requests
import mysql.connector 



def saveExceptions(number):

    myfile = open('exceptions.txt', 'w')
    # Creates numbers.txt file
    myfile.write(str(number) + '\n')
    myfile.close()



cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

''' api_request = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US" '''

'''If movie_id does not exist, the API returns the following json response:

{"success":false,"status_code":34,"status_message":"The resource you requested could not be found."}'''

movie_id = 1

while (movie_id <= 250000):


    ##############################################################################
    # API CALL TO RETRIEVE AND INSERT MOVIES, GENRES, PRODUCTION COMPANIES, 
    # PRODUCTION COUNTRIES AND SPOKEN LANGUAGES 
    ##############################################################################


    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US")
    data = response.json()
    #no matching movie_id
    if "success" in data:
        movie_id += 1
        continue

    '''DATA'''
    title               = data["title"]
    #inserted into movies table

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

    #inserted into genres
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

    #production_companies, movieprodcomp tables
    sqlprodcomp = "INSERT IGNORE INTO production_companies VALUES (%s, %s)"
    sqlmovie_prodcomp = "INSERT INTO movieprodcompanies (movie_id, production_company_id) VALUE (%s, %s)"
    for production_company in production_companies:
        prodcomp_data =  (production_company["id"], production_company["name"])
        movie_prodcomp_data = (movie_id, production_company["id"])
        cursor.execute(sqlprodcomp, prodcomp_data)
        cursor.execute(sqlmovie_prodcomp, movie_prodcomp_data)

    #production_countries, movieprodcountry tables
    sqlprodcountry = "INSERT IGNORE INTO production_countries VALUES (%s, %s)"
    sqlmovie_prodcountry = "INSERT INTO movieprodcountries (movie_id, production_country_id) VALUE (%s, %s)"
    for production_country in production_countries:
        # iso_3166_1 is unique identifier of countries, it's a string
        prodcountry_data =  (production_country["iso_3166_1"], production_country["name"])
        movie_prodcountry_data = (movie_id, production_country["iso_3166_1"])
        cursor.execute(sqlprodcountry, prodcountry_data)
        cursor.execute(sqlmovie_prodcountry, movie_prodcountry_data)

    #spoken_languages, moviespokenlang tables
    sqlspoken_langauges = "INSERT IGNORE INTO spoken_languages VALUES (%s, %s)"
    sqlmovie_spoken_language = "INSERT INTO moviespokenlanguages (movie_id, spoken_language_id) VALUE (%s, %s)"
    for spoken_language in spoken_languages:
        # iso_639_1 is a unique identifier for languages, it's a string
        spokenlang_data =  (spoken_language["iso_639_1"], spoken_language["name"])
        moviespokenlang_data = (movie_id, spoken_language["iso_639_1"])
        cursor.execute(sqlspoken_langauges, spokenlang_data)
        cursor.execute(sqlmovie_spoken_language, moviespokenlang_data)


    ##############################################################################
    # API CALL TO RETRIEVE AND INSERT MOVIE ACTORS AND CREW MEMBERS
    ##############################################################################

    
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US")

    data = response.json()

    cast = data["cast"]
    crew = data["crew"]

    for actor in cast:
        actor_id = actor["id"]
        name = actor["name"]
        original_name = actor["original_name"]
        known_for_department = actor["known_for_department"]
        gender = actor["gender"]
        popularity = actor["popularity"]


        sqlactors = "INSERT IGNORE INTO actors VALUES (%s, %s, %s, %s, %s ,%s)"
        actor_data = (actor_id, name, original_name, known_for_department, gender, popularity)
        cursor.execute(sqlactors, actor_data)

        sqlmovieactors = "INSERT INTO movieactors (movie_id, actor_id, character_name) VALUES (%s, %s, %s)"
        if actor["character"] != None:
            movie_characters = [c.lstrip(" ").rstrip(" ") for c in actor["character"].split("/")]
            for character in movie_characters:
                cursor.execute(sqlmovieactors, (movie_id, actor_id, character))
        else:
            cursor.execute(sqlmovieactors, (movie_id, actor_id, None))

    for member in crew:
        crew_id = member["id"]
        name = member["name"]
        original_name = member["original_name"]
        known_for_department = member["known_for_department"]
        gender = member["gender"]
        popularity = member["popularity"]

        department = member["department"]
        job = member["job"]

        sqlcrew = "INSERT IGNORE INTO crew VALUES (%s, %s, %s, %s, %s ,%s)"
        sqlmoviecrew = "INSERT IGNORE moviecrew (movie_id, crew_id, department, job) VALUES (%s, %s, %s, %s)"

        member_data = (crew_id, name, original_name, known_for_department, gender, popularity)

        cursor.execute(sqlcrew, member_data)
        cursor.execute(sqlmoviecrew, (movie_id, crew_id, department, job))

    

    cnx.commit()

    movie_id += 1


cnx.close()