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

sql = '''CREATE TABLE movieprodcountry(
    id NOT NULL AUTO INCREMENT PRIMARY INT,
    movieid INT,
    production_countryid INT
)'''

cursor.execute(sql)
cnx.close()


cnx.close()