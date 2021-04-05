USE stage_movies_db;

TRUNCATE TABLE stg_movies;
LOAD DATA INFILE 'D:/big_data/task3/data/movies.csv' 
INTO TABLE stg_movies 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;