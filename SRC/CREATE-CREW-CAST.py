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
'''
cursor.execute("DROP TABLE IF EXISTS actors")
cursor.execute("DROP TABLE IF EXISTS crew")
cursor.execute("DROP TABLE IF EXISTS moviecrew")
cursor.execute("DROP TABLE IF EXISTS movieactors")
'''

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