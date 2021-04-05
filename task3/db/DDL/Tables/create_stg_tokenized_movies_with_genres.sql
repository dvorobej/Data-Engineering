USE stage_movies_db;


DROP TABLE IF EXISTS stg_tokenized_movies_with_genres;
CREATE TABLE stg_tokenized_movies_with_genres(
	movie_id INT NOT NULL,
    movie_title VARCHAR(255) NOT NULL,
    movie_year INT NOT NULL,
    genre VARCHAR(255) NOT NULL,
    CONSTRAINT pk_movie_genre PRIMARY KEY (movie_id, genre)
);