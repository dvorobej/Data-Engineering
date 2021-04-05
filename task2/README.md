## Program structure

- main.py - source code file
- data_preprocessor.py - file with methods for getting/preprocessing data
- data_filters.py - file with methods to filter data
- command_parser.py - parser file
- data_reater.py - file with methods to read files
- data - directory with .csv files


## Used libraries (built-in)

- copy 
- re 2.2.1
- argparse 1.1

## Description
This program shows in the command line top n films by their rating and satisfying the filters specified on the command line.

## Execution
Program runs on the command line with parameters.
### Parameters
To get this message use the command from the working directory:
```
python main.py -h
```
```
usage: main.py [-h] [-N N] [-g GENRES] [-year_from YEAR_FROM]
               [-year_to YEAR_TO] [-regexp REGEXP]

optional arguments:
  -h, --help            show this help message and exit
  -N N                  number of films to show
  -g GENRES, --genres GENRES
                        filter by genres
  -year_from YEAR_FROM  year lower bound filter
  -year_to YEAR_TO      year upper bound filter
  -regexp REGEXP        name of the film filter
```

## Examples
### Show top 3 rated movies from 2000 to 2010 in genres (romance, drama, animation) with word death in their titles
```
python main.py -N 3 -year_from 2000 -year_to 2010 -g "drama|animation|romance"
```
![result](https://sun9-28.userapi.com/impg/-xo3S1GiVSdNJDQFW-efGN1B9c_16Cqojm2G0Q/42Nsx2_jjKQ.jpg?size=548x209&quality=96&sign=07884fb2278c2c45223679c93d188f39&type=album)
### Show top 10 movies in genre comedy
```
python main.py -N 10 -g comedy
```
![result](https://sun9-22.userapi.com/impg/p_SMx5RKkmBn-vMfDJQChgCNVhFpG-9_lDAY9w/brITV2494wQ.jpg?size=817x217&quality=96&sign=39f64b02f8150f89c8130b898a508821&type=album)