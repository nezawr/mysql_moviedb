USE DbMysql01;
SELECT movies.title, actors.name
FROM movies, actors, movieactors
WHERE movies.movie_id = movieactors.movie_id 
AND movieactors.actor_id = actors.actor_id;
