USE DbMysql01;
SELECT bestProdCompByGenre.genre AS genre, bestProdCompByGenre.prodCompName AS production_company,
		bestProdCompByGenre.occurrences AS CriteriaPassed
FROM
	(SELECT genre.name AS genre, prodComp.name AS prodCompName,  count(*) occurrences,
			ROW_NUMBER() OVER (PARTITION BY genre.name ORDER BY count(*) DESC) as pc_rank
	FROM 
	(SELECT DISTINCT production_companies.production_company AS name, movies.movie_id
		FROM movies, movieprodcompanies, production_companies
		WHERE movies.movie_id = movieprodcompanies.movie_id
		AND movieprodcompanies.production_company_id = production_companies.production_company_id
		AND movies.revenue - movies.budget >= 1000000) prodComp ,
		
	(SELECT DISTINCT genres.genre AS name, movies.movie_id
			FROM movies, genres, moviegenres
			WHERE movies.movie_id = moviegenres.movie_id
			AND moviegenres.genre_id = genres.genre_id) genre
	WHERE genre.movie_id = prodComp.movie_id
	GROUP BY genre, prodCompName
	ORDER BY occurrences DESC) bestProdCompByGenre
WHERE pc_rank <= 100
	AND genre = "Drama";