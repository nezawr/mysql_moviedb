USE DbMysql01;

SELECT concated_prodcomps.movie_title, crew.name AS Director, concated_genres.vote_average AS vote_average,
 concated_genres.revenue AS revenue, concated_genres.genres, concated_prodcomps.prodcomps
FROM
	(SELECT DISTINCT movies.title AS movie_title ,movies.movie_id AS movie_id, GROUP_CONCAT(production_companies.production_company) prodcomps
		 FROM movies, movieprodcompanies, production_companies
			   WHERE movies.overview  lIKE "%love%"
			   AND movies.movie_id = movieprodcompanies.movie_id
			   AND movieprodcompanies.production_company_id = production_companies.production_company_id
	 GROUP BY movies.movie_id) concated_prodcomps,
		
	(SELECT DISTINCT movies.movie_id AS movie_id, GROUP_CONCAT(genres.genre) genres, movies.revenue AS revenue,
		movies.vote_average AS vote_average
		FROM movies, moviegenres, genres
			WHERE movies.overview  lIKE "%love%"
            AND movies.movie_id = moviegenres.movie_id
            AND	moviegenres.genre_id = genres.genre_id
    GROUP BY movies.movie_id) concated_genres,
    
    (SELECT DISTINCT movies.movie_id AS movie_id, crew.name AS name
		FROM movies, moviecrew, crew
			WHERE movies.overview  lIKE "%love%"
            AND moviecrew.job = "Director"
            AND movies.movie_id = moviecrew.movie_id
            AND	moviecrew.crew_id = crew.crew_id
   ) crew
    
WHERE concated_genres.movie_id =  concated_prodcomps.movie_id
AND   crew.movie_id  = concated_prodcomps.movie_id

    