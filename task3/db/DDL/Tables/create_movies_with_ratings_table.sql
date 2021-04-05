USE movies_db;


DROP TABLE IF EXISTS movies_with_ratings;
CREATE TABLE movies_with_ratings(
	movie_id INT NOT NULL,
	movie_title TEXT NOT NULL,
    movie_year INT NOT NULL,
    genre VARCHAR(255) NOT NULL,
    rate FLOAT NOT NULL,
    CONSTRAINT pk_movie_genre PRIMARY KEY (movie_id, genre)
);
