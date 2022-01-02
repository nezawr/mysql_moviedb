import mysql.connector 

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

# MAIN TABLES - independent information
#cursor.execute("DROP TABLE IF EXISTS movies")
#cursor.execute("DROP TABLE IF EXISTS genres")
#cursor.execute("DROP TABLE IF EXISTS production_companies")
#cursor.execute("DROP TABLE IF EXISTS production_countries")
#cursor.execute("DROP TABLE IF EXISTS spoken_languages")


# CONNECTION TABLES - related information

#cursor.execute("DROP TABLE IF EXISTS moviegenres")
#cursor.execute("DROP TABLE IF EXISTS movieprodcompanies")
#cursor.execute("DROP TABLE IF EXISTS movieprodcountries")
#cursor.execute("DROP TABLE IF EXISTS moviespokenlanguages")

'''
cursor.execute("DROP TABLE IF EXISTS actors")
cursor.execute("DROP TABLE IF EXISTS crew")
cursor.execute("DROP TABLE IF EXISTS moviecrew")
cursor.execute("DROP TABLE IF EXISTS movieactors")
'''



sqlmovies = '''CREATE TABLE movies(
    movie_id INT NOT NULL PRIMARY KEY,
    title VARCHAR(250),
    adult BOOL,
    budget BIGINT,
    imdb_id VARCHAR(250),
    overview VARCHAR(1000),
    original_language CHAR(250),
    popularity INT,
    release_date VARCHAR(250),
    revenue BIGINT,
    status VARCHAR(250),
    vote_average FLOAT,
    vote_count INT,
    video VARCHAR(250)
)'''
cursor.execute(sqlmovies)


sqlgenres = '''CREATE TABLE genres(
    genre_id INT NOT NULL PRIMARY KEY, 
    genre VARCHAR(250)
)'''
cursor.execute(sqlgenres)



sqlproduction_companies = '''CREATE TABLE production_companies(
    production_company_id INT NOT NULL PRIMARY KEY,
    production_company VARCHAR(250)
)'''
cursor.execute(sqlproduction_companies)


sqlproduction_countries = '''CREATE TABLE production_countries(
    production_country_id VARCHAR(250) NOT NULL PRIMARY KEY,
    production_country VARCHAR(250)
)'''
cursor.execute(sqlproduction_countries)



sqlspoken_languages = '''CREATE TABLE spoken_languages(
    spoken_language_id VARCHAR(250) NOT NULL PRIMARY KEY,
    spoken_language VARCHAR(250)
)'''
cursor.execute(sqlspoken_languages)


sqlmoviegenres = '''CREATE TABLE moviegenres(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    genre_id INT
)'''
cursor.execute(sqlmoviegenres)



sqlmovieprodcompanies = '''CREATE TABLE movieprodcompanies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    production_company_id INT
)'''
cursor.execute(sqlmovieprodcompanies)



sqlmovieprodcountries = '''CREATE TABLE movieprodcountries(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    production_country_id VARCHAR(250)
)'''
cursor.execute(sqlmovieprodcountries)


sqlmoviespokenlanguages = '''CREATE TABLE moviespokenlanguages(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    spoken_language_id VARCHAR(250)
)'''
cursor.execute(sqlmoviespokenlanguages)


# MAIN TABLES - independent information


sqlactors = '''CREATE TABLE actors(
    actor_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(250),
    original_name VARCHAR(250),
    known_for_department VARCHAR(250),
    gender INT,
    popularity INT
)'''

cursor.execute(sqlactors)


sqlcrew = '''CREATE TABLE crew(
    crew_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(250),
    original_name VARCHAR(250),
    known_for_department VARCHAR(250),
    gender INT,
    popularity INT
)'''
cursor.execute(sqlcrew)


sqlmovieactors = '''CREATE TABLE movieactors(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    actor_id INT,
    character_name VARCHAR(250)
)'''
cursor.execute(sqlmovieactors)


sqlmoviecrew = '''CREATE TABLE moviecrew(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    crew_id INT,
    department VARCHAR(250),
    job VARCHAR(250)
)'''

cursor.execute(sqlmoviecrew)




cnx.close()