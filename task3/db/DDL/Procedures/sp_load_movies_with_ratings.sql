USE stage_movies_db;
DROP PROCEDURE IF EXISTS sp_load_movies_with_ratings;

DELIMITER $$

CREATE PROCEDURE sp_load_movies_with_ratings()
BEGIN
	CALL sp_load_tokenized_movies_table();
	CALL sp_load_table_with_splited_genres();
    TRUNCATE TABLE movies_db.movies_with_ratings;
    INSERT INTO movies_db.movies_with_ratings
	WITH temp_movies_with_ratings AS (
		SELECT m.movie_id, m.movie_title, m.movie_year, m.genre, ROUND(AVG(r.rating),3) as rate
		FROM stg_tokenized_movies_with_genres m
		INNER JOIN stg_ratings r ON r.movie_id = m.movie_id
		GROUP BY m.movie_id, m.genre, m.movie_title, m.movie_year
	)
	SELECT movie_id, movie_title, movie_year, genre, rate
	FROM temp_movies_with_ratings;
END $$

DELIMITER ;

