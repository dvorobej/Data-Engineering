# -*- coding: utf-8 -*-
"""
Version 1.1

@author: Dmitry Vorobey
"""


from data_preprocessor import (
    get_splited_by_genre_movies,
    get_sorted_by_rate_movies,
    get_most_popular_films,
    get_csv_like_data,
)
from command_parser import get_command_arguments
from data_reader import get_filtered_movies, get_filtered_movies_with_ratings


def print_data_in_command_line(data=[]):
    """
    Print data in the command line.
    
        Params:
            data (list): data to be printed
        
        Return value:
            None
    """
    for row in data:
        print(row)


def main():
    """
    Depending on the command line arguments print top popular films.

        Return value:
            None
    """
    command_args = get_command_arguments()

    number_of_films = command_args.N

    try:
        genres = list(map(str.capitalize, command_args.genres.strip(' "').split("|")))
    except:
        genres = command_args.genres

    year_from = command_args.year_from
    year_to = command_args.year_to

    try:
        regexp = command_args.regexp.strip("'\"")
    except:
        regexp = command_args.regexp

    movies = get_filtered_movies(
        year_from=year_from, year_to=year_to, genres=genres, regexp=regexp
    )

    if movies is None or len(movies) == 0:
        print("No movies found")
        return None

    movies = get_filtered_movies_with_ratings(filtered_movies=movies)

    if movies is None or len(movies) == 0:
        print("No ratings for movies were found")
        return None

    movies = get_splited_by_genre_movies(movies, genres)
    movies = get_sorted_by_rate_movies(movies)
    movies = get_most_popular_films(movies, number_of_films)

    data = get_csv_like_data(movies)

    # print result in command line
    print_data_in_command_line(data)


if __name__ == "__main__":
    main()
