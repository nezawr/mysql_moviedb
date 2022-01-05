USE DbMysql01;

SELECT earn.genre, count(earn.genre) c
FROM
(SELECT  genres.genre, movies.title, movies.revenue, movies.budget
FROM movies, moviegenres, genres
WHERE movies.movie_id = moviegenres.movie_id 
	 AND  moviegenres.genre_id = genres.genre_id
HAVING movies.revenue > 0 
	   AND movies.budget > 0
       AND movies.revenue - movies.budget > 10000000) earn
GROUP BY earn.genre
ORDER BY c DESC;