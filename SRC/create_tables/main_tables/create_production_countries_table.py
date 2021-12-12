import mysql.connector 

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

#cursor.execute("DROP TABLE IF EXISTS production_countries")
#{"success":false,"status_code":34,"status_message":"The resource you requested could not be found."}

sql = '''CREATE TABLE production_countries(
    production_country_id VARCHAR(250) NOT NULL PRIMARY KEY,
    production_country VARCHAR(250)
)'''

cursor.execute(sql)
cnx.close()