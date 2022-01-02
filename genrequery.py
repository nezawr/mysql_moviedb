import requests
import mysql.connector 

''' User inputs actor name and the query returns the movies in
    which this actor voice acted in   
'''

cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()

sqlgenres = (f"""
                SELECT genres.genre AS genre
                FROM genres;
                """)

cursor.execute(sqlgenres)
rows = cursor.fetchall()
for row in rows:
    print(row[0])

