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
cursor.execute("DROP TABLE IF EXISTS movies")
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


cursor.execute("DROP TABLE IF EXISTS genres")
sqlgenres = '''CREATE TABLE genres(
    genre_id INT NOT NULL PRIMARY KEY, 
    genre VARCHAR(250)
)'''
cursor.execute(sqlgenres)


cursor.execute("DROP TABLE IF EXISTS production_companies")
sqlproduction_companies = '''CREATE TABLE production_companies(
    production_company_id INT NOT NULL PRIMARY KEY,
    production_company VARCHAR(250)
)'''
cursor.execute(sqlproduction_companies)


cursor.execute("DROP TABLE IF EXISTS production_countries")
sqlproduction_countries = '''CREATE TABLE production_countries(
    production_country_id VARCHAR(250) NOT NULL PRIMARY KEY,
    production_country VARCHAR(250)
)'''
cursor.execute(sqlproduction_countries)


cursor.execute("DROP TABLE IF EXISTS spoken_languages")
sqlspoken_languages = '''CREATE TABLE spoken_languages(
    spoken_language_id VARCHAR(250) NOT NULL PRIMARY KEY,
    spoken_language VARCHAR(250)
)'''
cursor.execute(sqlspoken_languages)


# CONNECTION TABLES - related information

cursor.execute("DROP TABLE IF EXISTS moviegenres")
sqlmoviegenres = '''CREATE TABLE moviegenres(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    genre_id INT
)'''
cursor.execute(sqlmoviegenres)


cursor.execute("DROP TABLE IF EXISTS movieprodcompanies")
sqlmovieprodcompanies = '''CREATE TABLE movieprodcompanies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    production_company_id INT
)'''
cursor.execute(sqlmovieprodcompanies)


cursor.execute("DROP TABLE IF EXISTS movieprodcountries")
sqlmovieprodcountries = '''CREATE TABLE movieprodcountries(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    production_country_id VARCHAR(250)
)'''
cursor.execute(sqlmovieprodcountries)

cursor.execute("DROP TABLE IF EXISTS moviespokenlanguages")
sqlmoviespokenlanguages = '''CREATE TABLE moviespokenlanguages(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    spoken_language_id VARCHAR(250)
)'''
cursor.execute(sqlmoviespokenlanguages)

cnx.close()









cnx.close()