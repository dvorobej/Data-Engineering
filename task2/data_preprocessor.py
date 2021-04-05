# -*- coding: utf-8 -*-
"""
Version 1.1

@author: Dmitry Vorobey
"""

import re
from copy import deepcopy


def get_csv_like_data(movies, symbol=','):
    """
    Get data in convenient format.
    
        Params:
            movies (dict): movies data
        
        Return value:
            data (list): data separated by symbol
    """
    data = []
    
    data.append(['genre','name','year','rate'])
    
    for key in movies.keys(): # key=genre
        for movie in movies[key]: #movie=[movie_name, movie_year, movie_rate]
            data.append([key, movie[0], str(movie[1]), str(movie[2])])
    
    for movie in range(len(data)): 
        #data[movie] = [genre, movie_name, movie_year, movie_rate]
        if symbol in data[movie][1]:
            data[movie][1] = '"' + data[movie][1] + '"'
        data[movie] = symbol.join(data[movie])
        
    return data


def get_most_popular_films(sorted_movies, n=None):
    """
    Get n most popular (by their rate) films.
    
        Params:
            sorted_movies (dict): sorted by their rate movies
            n (int): number of films to get
        
        Return value:
            top_movies (dict): top n movies
    """
    top_movies = {}
    
    if n is None:
        top_movies = deepcopy(sorted_movies)
        return top_movies
    
    for key in sorted_movies.keys():
        if len(sorted_movies[key]) < n:
            top_movies[key] = sorted_movies[key].copy()
        else:
            top_movies[key] = sorted_movies[key][:n]
    
    return top_movies


def get_filtered_genres(film_genres, desired_genres=None):
    """
    Get film genres satisfies desired genres.
    
        Params:
            film_genres (list): movie's genres
            desired_genres (list): wanted genres
            
        Return value:
             filtered_genres (list): genres in the movie satisfing desired genres
    """
    filtered_genres = []
    
    if desired_genres is None:
        filtered_genres = None
    
    else:
        for genre in desired_genres:
            if (genre in film_genres) and (genre not in filtered_genres):
                filtered_genres.append(genre)
    
    return filtered_genres


def get_splited_by_genre_movies(movies_with_ratings, genres=None):
    """
    Get movies splited by desired genres.
    
        Params:
            movies_with_ratings (list): movies with their ratings
            genres (list): wanted genres
            
        Return value:
            splited_movies (dict): movies splited by genre
    """
    movies_with_ratings = deepcopy(movies_with_ratings)
    splited_movies = {}
    
    if genres is None:
        splited_movies[''] = []
        for movie in range(len(movies_with_ratings)):
            # movies_with_ratings[movie] = [movie_name, movie_year, movie_genres, movie_rate]
            splited_movies[''].append([movies_with_ratings[movie][0],
                                                movies_with_ratings[movie][1], 
                                                movies_with_ratings[movie][3]])
        return splited_movies
    
    for genre in genres:
        splited_movies[genre] = []
    
    for movie in range(len(movies_with_ratings)):
        for genre in genres:
            if genre in movies_with_ratings[movie][2]:
                # movies_with_ratings[movie] = [movie_name, movie_year, movie_genres, movie_rate]
                splited_movies[genre].append([movies_with_ratings[movie][0], 
                                              movies_with_ratings[movie][1], 
                                              movies_with_ratings[movie][3]])
    
    return splited_movies


def get_sorted_by_rate_movies(movies, reverse=True):
    """
    Get movies sorted by their rate.
    
        Params:
            movies (dict): movies splited by genre
            reverse (bool): flat to sort desc/asc
            
        Return value:
            sorted_movies (dict): movies sorted by their rate
    """
    sorted_movies = deepcopy(movies)
    
    for i in sorted_movies.keys():
        sorted_movies[i] = sorted(sorted_movies[i], 
                                  key = lambda pair: pair[2], 
                                  reverse=True)
        
    return sorted_movies


def get_movie_year(film):
    """
    Get movies's release year.
    
        Params:
            film (str): string with film name and year
        
        Return value:
            year (int): movie's release year
    """
    # delete posible spaces and quotes
    film = film.strip(" \"").strip(" \"")
    
    try:
        years = re.findall('[(]\d+[^()]*\d+[)]$', film)[0]
        years = re.findall('\d\d\d\d', years)
        years = list(map(int, years))
        year = max(years)
        return year
    
    # except works if date wasn't found in film
    except:
        return None


def get_movie_name(film):
    """
    Get movie's name.
    
        Params:
            film (str): string with film name and year
        
        Return value:
            name (int): movie's name
    """
    # delete posible spaces and quotes
    film = film.strip(" \"").strip(" \"")
    
    try:
        years_len = len(re.findall('[(]\d+[^()]*\d+[)]$', film)[0])
        name = film[:-years_len].strip()
        return name
    
    # except works if date wasn't found in film
    except:
        return None


def get_symbol_positions(text, symbol=',', ignore=''):
    """
    Get positions of the symbol in the text.
    
        Params:
            symbol (str): desired symbol
            text (str): text
            ignore (str): symbol between which we ignore desired symbol
        Return value:
            symbol_positions (list): positions of the symbol
    """
    symbol_positions = []
    
    try:
        # find desired symbol positions   
        for i in range(len(text)):
            if text[i] == symbol:
                symbol_positions.append(i)
                
        # find ignore symbol positions
        if ignore != '':
            ignore_positions = []
            for i in range(len(text)):
                if text[i] == ignore:
                    ignore_positions.append(i)
        
            # check ingore list
            if (len(ignore_positions)%2 != 0) and (len(ignore_positions) != 0):
                ignore_positions.pop()
                
            # filter desired symbols by ignore
            filtered_symbol_positions = []
            
            for symbol in symbol_positions:
                for i in range(0, len(ignore_positions)-1, 2):
                    if ignore_positions[i] < symbol < ignore_positions[i+1]:
                        break
                else:
                    filtered_symbol_positions.append(symbol)
            
            return filtered_symbol_positions
        
        return symbol_positions
    except:
        return None
    
    
def get_tokens(text, sep=',', ignore='"'):
    """
    Get tokens of the text with ',' as separator.
    
        Params:
            text (str): text for tokenization
            sep (str): symbol to use for tokenization
            ignore (str): symbol between which we ignore desired symbol
        
        Return value:
            tokens (list): list of tokens
    """
    comma_positions = get_symbol_positions(text, symbol=sep, ignore=ignore)
    
    # Return None if we have problems with commas
    if comma_positions is None:
        return None
    
    # If symbol was not found
    if len(comma_positions) == 0:
        return [text]
    
    try:
        tokens = []
    
        tokens.append(text[:comma_positions[0]])
        for i in range(len(comma_positions)):
            if i == len(comma_positions) - 1:
                tokens.append(text[comma_positions[i]+1:-1]) # -1 because of \n 
            else:
                tokens.append(text[comma_positions[i]+1:comma_positions[i+1]])
                
        return tokens
    except:
        return None
    
    
def get_movie_params(row):
    """
    Get movie parameters from the tokenized row.
    
        Params:
            row (list): tokenized string
        
        Return value:
            movie_id (int): movie's id
            movie_year (int): movie's year
            movie_name (str): movie's name
            movie_genres (list): movie's genres
    """    
    try:
        movie_id = int(row[0].strip())
    except:
        return None
                
    movie_name = get_movie_name(row[1])
    movie_year = get_movie_year(row[1])
            
    # Transform all genres to the similar form
    try:
        movie_genres = list(map(str.capitalize, 
                                list(map(str.strip,row[2].strip().split('|')))))
    except:
        movie_genres = None
    
    return movie_id, movie_year, movie_name, movie_genres


def get_rating_params(row):
    """
    Get rating parameters from the tokenized row.
    
        Params:
            row (list): tokenized string
        
        Return value:
            user_id (int): user's id
            movie_id (int): movie's id
            rating (float): movie's rating
    """
    try:
        user_id = int(row[0].strip())
    except:
        return None
    
    try:
        movie_id = int(row[1].strip())
    except:
        return None
    
    try:
        rating = float(row[2].strip())
    except:
        return None
    
    return user_id, movie_id, rating



def update_movie_ratings(filtered_movies, movie_id, rating):
    """
    Update movies ratings if filtered_movies.
    
        Params:
            movie_id (int): movie's id
            rating (float): movie's rating
        
        Return value:
            None
    """
    for i in range(len(filtered_movies)):
        if filtered_movies[i][0] == movie_id:
            filtered_movies[i][4] += rating
            filtered_movies[i][5] += 1 # number of reviews
            
    return None