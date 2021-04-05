USE movies_db;


DROP PROCEDURE IF EXISTS sp_find_top_rated_movies;

DELIMITER $$

CREATE PROCEDURE sp_find_top_rated_movies(IN number_of_films INT, IN title_filter TEXT,IN year_from INT,IN year_to INT,IN genres TEXT)
BEGIN	
	WITH cte AS (
		WITH filtered_movies AS (
			SELECT movie_title, movie_year, genre, rate, movie_id
			FROM movies_with_ratings
			WHERE 
				(title_filter IS NULL OR movie_title REGEXP title_filter)
				AND
				((year_from IS NULL OR movie_year >= year_from) 
				AND 
				(year_to IS NULL OR movie_year <= year_to))
				AND
				(genres IS NULL OR genres REGEXP genre)
		)
		SELECT 
			genre, movie_title, movie_year, rate,
			ROW_NUMBER() OVER (PARTITION BY genre ORDER BY rate DESC, movie_id) rate_number
		FROM filtered_movies
	)
	SELECT genre, movie_title, movie_year, rate
	FROM cte
	WHERE (number_of_films IS NULL OR rate_number <= number_of_films);
END $$

DELIMITER ;

CALL sp_find_top_rated_movies(NULL, NULL, NULL, NULL, NULL);