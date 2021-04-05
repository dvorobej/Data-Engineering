USE stage_movies_db;


DROP TABLE IF EXISTS stg_movies;
CREATE TABLE stg_movies(
	movie_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    genres VARCHAR(255) NOT NULL,
    CONSTRAINT pk_movie_id PRIMARY KEY (movie_id)
);
