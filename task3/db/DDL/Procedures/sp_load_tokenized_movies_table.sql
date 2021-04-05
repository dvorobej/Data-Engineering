USE stage_movies_db;
DROP PROCEDURE IF EXISTS sp_load_tokenized_movies_table;

DELIMITER $$

CREATE PROCEDURE sp_load_tokenized_movies_table()
BEGIN
	TRUNCATE TABLE stage_movies_db.stg_tokenized_movies;
    INSERT INTO stage_movies_db.stg_tokenized_movies
	SELECT 
		movie_id,
		CONVERT(SUBSTR(REGEXP_SUBSTR(title, '[(]\\d+[^()]*\\d+[)]$'),-5, 4), UNSIGNED INTEGER) movie_year,
		TRIM(REGEXP_REPLACE(title, '[(]\\d+[^()]*\\d+[)]$','')) movie_title,
		genres
	FROM stg_movies
	WHERE 
		CONVERT(SUBSTR(REGEXP_SUBSTR(title, '[(]\\d+[^()]*\\d+[)]$'),-5, 4), UNSIGNED INTEGER) IS NOT NULL
		AND
		TRIM(REGEXP_REPLACE(title, '[(]\\d+[^()]*\\d+[)]$','')) IS NOT NULL
		AND genres <> '(no genres listed)';
END $$

DELIMITER ;