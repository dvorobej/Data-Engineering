# -*- coding: utf-8 -*-
"""
Version 1.0

@author: Dmitry Vorobey
"""


from data_preprocessor import (
    get_movie_params,
    get_tokens,
    update_movie_ratings,
    get_rating_params,
)
from data_filters import (
    check_all_movie_filters,
    check_movies_csv_row,
    check_rating_csv_row,
)
from copy import deepcopy
import os

def get_filtered_movies(
    path="data/movies.csv", year_from=None, year_to=None, regexp=None, genres=None
):
    """
    Get filtered movies from path file.
        Params:
            path (str): path to movies.csv
            year_from (int): from what year film
            year_to (int): to what year film
            regexp (str): movie's name filter
            genres (list): wanted genres
        Return value:
            filtered_movies (list): movies satisfying all filters
    """
    filtered_movies = []
    number_of_columns_in_file = 3
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, path)

    try:
        with open(path, encoding='utf-8') as file:
            
            # skip title
            file.readline()
            for string in file:
                row = get_tokens(string)

                # check tokenization
                if len(row) != number_of_columns_in_file:
                    continue

                movie_id, movie_year, movie_name, movie_genres = get_movie_params(row)

                # check if data is clean
                if not check_movies_csv_row(
                    id=movie_id, name=movie_name, year=movie_year, genres=movie_genres
                ):
                    continue

                # use filters
                if not check_all_movie_filters(
                    movie_name=movie_name,
                    movie_year=movie_year,
                    movie_genres=movie_genres,
                    year_from=year_from,
                    year_to=year_to,
                    genres=genres,
                    regexp=regexp,
                ):
                    continue

                # add filtered data 
                # [movie_id, movie_name, movie_year, movie_genres, movie_rate, number_of_reviews]
                filtered_movies.append(
                    [movie_id, movie_name, movie_year, movie_genres, 0.0, 0.0]
                )

        return filtered_movies
    except Exception as e:
        print(e)
        return None


def get_filtered_movies_with_ratings(path="data/ratings.csv", filtered_movies=None):
    """
    Get movies with their ratings.

        Params:
            path (str): path to ratings.csv
            filtered_movies (list): movies

        Return value:
            movies_with_ratings (list): movies with their ratings
    """
    if filtered_movies is None:
        return None

    filtered_movies = deepcopy(filtered_movies)
    movies_with_ratings = []
    number_of_columns_in_file = 4
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, path)

    try:
        with open(path, encoding='utf-8') as file:
            
            # skip title
            file.readline()
            for string in file:
                row = get_tokens(string)

                # check tokenization
                if len(row) != number_of_columns_in_file:
                    continue

                user_id, movie_id, rating = get_rating_params(row)

                if not check_rating_csv_row(
                    user_id=user_id, movie_id=movie_id, rating=rating
                ):
                    continue

                update_movie_ratings(
                    filtered_movies=filtered_movies, movie_id=movie_id, rating=rating
                )
        # set ratings to movies
        # [movie_id, movie_name, movie_year, movie_genres, movie_rate, number_of_reviews]
        for movie in range(len(filtered_movies)):
            if filtered_movies[movie][5] != 0:
                movies_with_ratings.append(
                    [
                        filtered_movies[movie][1],
                        filtered_movies[movie][2],
                        filtered_movies[movie][3],
                        round(filtered_movies[movie][4] / filtered_movies[movie][5], 3),
                    ]
                )
        return movies_with_ratings
    except Exception as e:
        print(e)
        return None

