import mysql.connector 

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

#cursor.execute("DROP TABLE IF EXISTS production_companies")
#{"success":false,"status_code":34,"status_message":"The resource you requested could not be found."}

sql = '''CREATE TABLE production_companies(
    production_company_id INT NOT NULL PRIMARY KEY,
    production_company VARCHAR(250)
)'''

cursor.execute(sql)
cnx.close()