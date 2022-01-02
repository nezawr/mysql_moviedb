USE DbMysql01;
SELECT bestProdByLanguage.ol AS language, bestProdByLanguage.pc AS productionCompany, bestProdByLanguage.occurrences As CriteriaPassed
FROM 
(SELECT ProdByLanguage.pc AS pc , ProdByLanguage.ol AS ol, count(*) occurrences,
	ROW_NUMBER() OVER (PARTITION BY ProdByLanguage.ol ORDER BY count(*) DESC) as pc_rank
FROM
	( SELECT movies.original_language AS ol, production_companies.production_company AS pc
		FROM movies, movieprodcompanies, production_companies
		WHERE movies.movie_id = movieprodcompanies.movie_id
		AND movieprodcompanies.production_company_id = production_companies.production_company_id
		AND movies.revenue - movies.budget >= 10000000) ProdByLanguage
GROUP BY ol, pc
ORDER BY occurrences DESC) bestProdByLanguage
WHERE pc_rank <= 3;


# ROW_NUMBER() OVER (PARTITION BY bestProdByLanguage.production_company, bestProdByLanguage.original_language ORDER BY count(*) DESC) as pc_rank



