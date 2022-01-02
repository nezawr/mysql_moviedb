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


#QUERY 1 
''' User inputs actor name and the query returns the movies in
    which this actor voice acted in   
'''

actor_name = "Brad Pitt"

sql_voice_actor = (f"""
                SELECT actors.name AS actor_name, movies.title AS movie_title, movieactors.character_name AS character_name
                FROM actors, movies, movieactors
                WHERE movieactors.character_name LIKE '%Voice%'
	                AND movies.movie_id = movieactors.movie_id
                    AND movieactors.actor_id = actors.actor_id
                    AND actors.name = "{actor_name}"
                """)


#QUERY 2
''' User inputs genre name, vote count, average rating, the difference between
    the movie revenue and budget and the query returns the genre, the name of the best production company how many movies it produced matched the criteria. 

    Genres:    Adventure, Fantasy, Animation, Drama, Horror, Action, Comedy, History, Western,
                        Thriller, Crime, Documentary, Science Fiction, Mystery, Music, Romance,
                        Family, War, TV Movie 
    Vote Count:  Positive Integer
    vote Average: 0 < x <= 10
    revenvue - budget: Positive integer
'''

sql_bestprodcomp_bygenre = (f"""
                SELECT actors.name AS actor_name, movies.title AS movie_title, movieactors.character_name AS character_name
                FROM actors, movies, movieactors
                WHERE movieactors.character_name LIKE '%Voice%'
	                AND movies.movie_id = movieactors.movie_id
                    AND movieactors.actor_id = actors.actor_id
                    AND actors.name = "{actor_name}"
                """)



cursor.execute(sqlmovie_id)
rows = cursor.fetchall()
for row in rows:
    print(row)

cnx.close()