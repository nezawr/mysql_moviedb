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

sqlmovie_id = ("""
                SELECT movie_id
                FROM movies
                WHERE movie_id >= 22066
                """)

cursor.execute(sqlmovie_id)
rows = cursor.fetchall()
for row in rows:

    movie_id = row[0]
    print(movie_id)
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=dc5ea0a6055e40034e3a85d8c9c511b8&language=en-US")

    data = response.json()

    cast = data["cast"]
    crew = data["crew"]

    for actor in cast:
        actor_id = actor["id"]
        name = actor["name"]
        original_name = actor["original_name"]
        known_for_department = actor["known_for_department"]
        gender = actor["gender"]
        popularity = actor["popularity"]


        sqlactors = "INSERT IGNORE INTO actors VALUES (%s, %s, %s, %s, %s ,%s)"
        actor_data = (actor_id, name, original_name, known_for_department, gender, popularity)
        cursor.execute(sqlactors, actor_data)

        sqlmovieactors = "INSERT INTO movieactors (movie_id, actor_id, character_name) VALUES (%s, %s, %s)"
        if actor["character"] != None:
            movie_characters = [c.lstrip(" ").rstrip(" ") for c in actor["character"].split("/")]
            for character in movie_characters:
                cursor.execute(sqlmovieactors, (movie_id, actor_id, character))
        else:
            cursor.execute(sqlmovieactors, (movie_id, actor_id, None))

    for member in crew:
        crew_id = member["id"]
        name = member["name"]
        original_name = member["original_name"]
        known_for_department = member["known_for_department"]
        gender = member["gender"]
        popularity = member["popularity"]

        department = member["department"]
        job = member["job"]

        sqlcrew = "INSERT IGNORE INTO crew VALUES (%s, %s, %s, %s, %s ,%s)"
        sqlmoviecrew = "INSERT IGNORE moviecrew (movie_id, crew_id, department, job) VALUES (%s, %s, %s, %s)"

        member_data = (crew_id, name, original_name, known_for_department, gender, popularity)

        cursor.execute(sqlcrew, member_data)
        cursor.execute(sqlmoviecrew, (movie_id, crew_id, department, job))

    cnx.commit()


cnx.close()

  

