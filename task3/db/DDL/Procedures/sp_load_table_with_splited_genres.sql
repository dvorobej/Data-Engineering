USE stage_movies_db;
DROP PROCEDURE IF EXISTS sp_load_table_with_splited_genres;

DELIMITER $$

CREATE PROCEDURE sp_load_table_with_splited_genres()
BEGIN
	TRUNCATE TABLE stage_movies_db.stg_tokenized_movies_with_genres;
	INSERT INTO stage_movies_db.stg_tokenized_movies_with_genres
	WITH RECURSIVE temp_movies_with_genres (movie_id, movie_title, movie_year, genre, left_genres) AS
	(
		SELECT
			movie_id,
			movie_title,
			movie_year,
			SUBSTRING_INDEX(CONCAT(genres, '|'),'|',1) as genre,
			SUBSTR(CONCAT(genres, '|'), INSTR(CONCAT(genres,'|'),'|')+1) as left_genres
		FROM stg_tokenized_movies
		UNION ALL
		SELECT
			movie_id,
			movie_title,
			movie_year,
			SUBSTRING_INDEX(left_genres,'|',1) as genre,
			SUBSTR(left_genres, INSTR(left_genres,'|')+1) as left_genres
		FROM temp_movies_with_genres
		WHERE left_genres <> '' AND left_genres IS NOT NULL
	)
	SELECT movie_id, movie_title, movie_year, genre
	FROM temp_movies_with_genres;
END $$

DELIMITER ;