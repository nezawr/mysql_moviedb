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

sql = '''CREATE TABLE movies(
    movie_id INT NOT NULL PRIMARY KEY,
    title VARCHAR(250),
    adult BOOL,
    budget INT,
    imdb_id VARCHAR(250),
    overview VARCHAR(1000),
    original_language CHAR(250),
    popularity INT,
    release_date VARCHAR(250),
    revenue INT,
    status VARCHAR(250),
    vote_average FLOAT,
    vote_count INT,
    video VARCHAR(250)
)'''

cursor.execute(sql)

cnx.close()