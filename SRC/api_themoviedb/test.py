import requests
import mysql.connector 


cnx = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql01',
    password='DbMysql01',
    database='DbMysql01'
)

cursor = cnx.cursor()


response = requests.get(f"https://api.themoviedb.org/3/movie/{35}/credits?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US")


data = response.json()
cast = data["cast"]

for actor in cast:
    x = [c.lstrip(" ").rstrip(" ") for c in actor["character"].split("/")]
    for p in x:
        print(p)