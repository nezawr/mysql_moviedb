Use DbMysql01;

SELECT filtered_crew.name , filtered_crew.popularity

FROM
	(SELECT DISTINCT movies.movie_id AS movie_id, production_companies.production_company AS name
	 FROM movies, movieprodcompanies, production_companies
		   WHERE movies.movie_id = movieprodcompanies.movie_id
		   AND movieprodcompanies.production_company_id = production_companies.production_company_id
		   AND production_companies.production_company = "Universal Pictures") filtered_production_companies,
           
	(SELECT DISTINCT movies.movie_id AS movie_id, crew.name AS name, crew.popularity AS popularity
	 FROM movies, moviecrew, crew
		  WHERE crew.popularity >= 3
          AND moviecrew.job = "Director"
          AND movies.movie_id = moviecrew.movie_id
          AND moviecrew.crew_id = crew.crew_id
          ) filtered_crew
          
WHERE filtered_production_companies.movie_id = filtered_crew.movie_id
ORDER BY filtered_crew.popularity DESC; 
       

	 

	 