USE stage_movies_db;


DROP TABLE IF EXISTS stg_tokenized_movies;
CREATE TABLE stg_tokenized_movies(
	movie_id INT NOT NULL,
    movie_year INT NOT NULL,
    movie_title VARCHAR(255) NOT NULL,
    genres VARCHAR(255) NOT NULL,
    CONSTRAINT pk_movie_id PRIMARY KEY (movie_id)
);