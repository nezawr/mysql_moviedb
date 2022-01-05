USE DbMysql01;
SELECT actor.name,  crewmember.name, count(*) as bestPair
FROM
(SELECT movies.movie_id, actors.name, movies.vote_average, movies.vote_count
 FROM movies, actors, movieactors
 WHERE movies.movie_id = movieactors.movie_id
 AND movieactors.actor_id = actors.actor_id
 AND movies.vote_count >= 2500 AND movies.vote_average >= 8.5) actor,
 (SELECT movies.movie_id, crew.name, movies.revenue, movies.budget
  FROM movies, moviecrew, crew
  WHERE movies.movie_id = moviecrew.movie_id 
  AND moviecrew.job = "Director"
  AND   moviecrew.crew_id = crew.crew_id
  AND movies.revenue - movies.budget > 1000000) crewmember
WHERE actor.movie_id = crewmember.movie_id
GROUP BY actor.name,  crewmember.name
ORDER BY bestPair DESC;

