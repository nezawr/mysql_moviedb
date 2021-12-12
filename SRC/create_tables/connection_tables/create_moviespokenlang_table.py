import mysql.connector 

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

#cursor.execute("DROP TABLE IF EXISTS moviespokenlanguages")
#{"success":false,"status_code":34,"status_message":"The resource you requested could not be found."}

sql = '''CREATE TABLE moviespokenlanguages(
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    spoken_language_id VARCHAR(250)
)'''

cursor.execute(sql)
cnx.close()


cnx.close()