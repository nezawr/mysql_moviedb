SELECT actors.name AS actor_name, movies.title AS movie_title, movieactors.character_name AS character_name
FROM actors, movies, movieactors
WHERE movieactors.character_name LIKE '%Voice%'
	  AND movies.movie_id = movieactors.movie_id
      AND movieactors.actor_id = actors.actor_id
      #AND movies.overview LIKE '%sex%'
      #AND actos.name = "PUT ACTOR NAME HERE"