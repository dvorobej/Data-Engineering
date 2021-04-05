USE stage_movies_db;

TRUNCATE TABLE stg_ratings;
LOAD DATA INFILE 'D:/big_data/task3/data/ratings.csv' 
INTO TABLE stg_ratings
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS; 