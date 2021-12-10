import mysql.connector 

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

#cursor.execute("DROP TABLE IF EXISTS movies")
#{"success":false,"status_code":34,"status_message":"The resource you requested could not be found."}

sql = '''CREATE TABLE spoken_languages(
    movie_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(200),
    adult BOOL,
    budget INT,
    imdb_id VARCHAR(200),
    overview VARCHAR(1000),
    original_language CHAR(200),
    popularity INT,
    release_date VARCHAR(200),
    revenue INT,
    status VARCHAR(200),
    vote_average FLOAT,
    vote_count INT,
    video VARCHAR(200)
)'''

cursor.execute(sql)


cnx.close()