# -*- coding: utf-8 -*-
"""
Version 1.1

@author: Dmitry Vorobey
"""

def check_genres_filter(film_genres, filter_genres=None):
    """
    Check if film_genres satisfies desired genres.
    
        Params:
            film_genres (list): movie's genres
            filter_genres (list): wanted genres
            
        Return value:
            (bool): if film_genres satisfies filter genres
    """    
    if filter_genres is None:
        return True
    else:
        for genre in filter_genres:
            if genre in film_genres:
                return True
            
    return False


def check_name_filter(film_name, regexp=None):
    """
    Check if film_name satisfies regexp.
    
        Params:
            film_name (str): movie's name
            regexp (str): movie's name filter
        
        Return value:
            (bool): if film_name satisfies name filter
    """
    if regexp is None:
        return True        
    else:
        if regexp.lower() in film_name.lower():
            return True
        
    return False


def check_year_filter(film_year, year_from=None, year_to=None):
    """
    Check if film_year satisfies time limits.
    
        Params:
            film_year (int): movie's release year
            year_from (int): from what year film
            year_to (int): to what year film
            
        Return value:
            (bool): if film_year satisfies time limits
    """    
    if (year_from is None) and (year_to is None):
        return True
    
    elif year_from is None:
        if film_year <= year_to:
            return True
            
    elif year_to is None:
        if film_year >= year_from:
            return True
    
    else:
        if year_from <= film_year <= year_to:
            return True
    
    return False


def check_movies_csv_row(id, name, year, genres):
    """
    Check if row from movies.csv has unclean data.
    
        Params:
            id (int): movie's id
            name (str): movie's name
            year (str): movie's release year
            genres (list): movie's genres
        
        Return value:
            (bool): is data clean
    """    
    # check None values in params
    if None in (id, name, year, genres):
        return False
    
    # check if data has genres
    if len(genres) == 0:
        return False
    
    if len(genres) == 1 and genres[0] == '(no genres listed)':
        return False
    
    return True


def check_rating_csv_row(user_id, movie_id, rating):
    """
    Check if row from rating.csv has unclean data.
    
        Params:
            user_id (int): user's id
            movie_id (int): movie's id
            rating (str): movie's rating
        
        Return value:
            (bool): is data clean
    """    
    # check None values in params
    if None in (user_id, movie_id, rating):
        return False
    
    # check rating values
    if rating < 0 or rating > 5:
        return False
        
    return True

def check_all_movie_filters(movie_name, movie_year, movie_genres, year_from, year_to, genres, regexp):
    """
    Check if movie satisfies all the filters.
    
        Params:
            movie_name (str): movie's name
            movie_year (int): movie's release year
            movie_genres (list): movie's genres
            year_from (int): from what year film
            year_to (int): to what year film
            genres (list): wanted genres
            regexp (str): movie's name filter
        
        Return value:
            (bool): if movie satisfies all the filters
    """    
    # check year filter
    if not check_year_filter(movie_year, year_from, year_to):
        return False
            
    # check name filter
    if not check_name_filter(movie_name, regexp):
        return False
                
    # check genres filter
    if not check_genres_filter(movie_genres, genres):
        return False
    
    return True
