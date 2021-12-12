import mysql.connector 

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

#cursor.execute("DROP TABLE IF EXISTS spoken_languages")
#{"success":false,"status_code":34,"status_message":"The resource you requested could not be found."}

sql = '''CREATE TABLE spoken_languages(
    spoken_language_id VARCHAR(250) NOT NULL PRIMARY KEY,
    spoken_language VARCHAR(250)
)'''

cursor.execute(sql)
cnx.close()


cnx.close()