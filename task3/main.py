# -*- coding: utf-8 -*-
"""
Version 1.1

@author: Dmitry Vorobey
"""

import mysql.connector
import argparse


def get_command_arguments():
    """
    Get the arguments from the command line.

        Return value:
            command_args (argparse.Namespace): arguments of the command line
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-N", type=int, help="number of films to show")
    parser.add_argument("-g", "--genres", type=str, help="filter by genres")
    parser.add_argument("-year_from", type=int, help="year lower bound filter")
    parser.add_argument("-year_to", type=int, help="year upper bound filter")
    parser.add_argument("-regexp", type=str, help="name of the film filter")
    parser.add_argument("-user", default="root", type=str, help="username in mysql")
    parser.add_argument("-pswd", default="3110", type=str, help="password in mysql")
    parser.add_argument(
        "-host", default="localhost", type=str, help="host name in mysql"
    )
    parser.add_argument("-port", default="3306", type=str, help="port in mysql")
    parser.add_argument("-db", default='movies_db', type=str, help='database name')

    command_args = parser.parse_args()

    return command_args


def print_movies_in_command_line(movies):
    """
    Print data in the command line.
    
        Params:
            movies (list): movies to be printed
        
        Return value:
            None
    """
    print("genre,title,year,rating")
    # movie = [movie_genre(str), movie_title (str), movie_year (int),  movie_rating(float)]
    for movie in movies:
        print(f'{movie[0]},{movie[1]},{movie[2]},{movie[3]}')
    print(len(movies))


def main():
    """
    Depending on the command line arguments print top popular films.

        Return value:
            None
    """
    command_args = get_command_arguments()
    
    # connect to movied_db in mysql
    try:
        mydb = mysql.connector.connect(
            host=command_args.host,
            port=command_args.port,
            user=command_args.user,
            passwd=command_args.pswd,
            database=command_args.db
        )
        
        cursor = mydb.cursor()
    except Exception as e:
        print(e)
        return None

    query_params = [command_args.N,
                    command_args.regexp,
                    command_args.year_from,
                    command_args.year_to,
                    command_args.genres]
    
    # call stored procedure
    try:
        cursor.callproc('sp_find_top_rated_movies', query_params)
    except Exception as e:
        print(e)
        return None
            
    
    for result in cursor.stored_results():
        results = result.fetchall()
        
    print_movies_in_command_line(results)
    
    # close conection
    try:
        cursor.close()
        mydb.close() 
    except Exception as e:
        print(e)
        return None
    
if __name__ == '__main__':
    main()

