USE stage_movies_db;


DROP TABLE IF EXISTS stg_ratings;
CREATE TABLE stg_ratings(
	user_id INT NOT NULL,
    movie_id INT NOT NULL,
    rating FLOAT NOT NULL,
    timestamp INT NOT NULL,
    CONSTRAINT pk_user_movie_id PRIMARY KEY (user_id, movie_id)
);