## Program structure

- main.py - source code file
- setup_environment.py - file for creating and configuring the database
- db - directory with .sql files
	- DDL - directory with .sql files for creating database objects
		- Databases - directory with .sql files for creating databases
		- Tables - directory with .sql files for creating tables
		- Procedures - directory with .sql files for creating stored procedures
	- DML - directory with .sql files for manipulating data
		- Filling-tables - directory with .sql files for filling tables
- data - directory with .csv files


## Used libraries

- os (built-in)
- argparse 1.1 (built-in)
- mysql.connector 8.0.23

## Libraries installation
```
pip install -r requirements.txt
```

## Description
Program to find movie(s) with filtering out movies by genre(s), title and year.

## Execution
Program runs on the command line with parameters.
### Parameters
To get this message use the command from the working directory:
```
python main.py -h
```
```
usage: main.py [-h] [-N N] [-g GENRES] [-year_from YEAR_FROM]
               [-year_to YEAR_TO] [-regexp REGEXP] [-user USER] [-pswd PSWD]
               [-host HOST] [-port PORT] [-db DB]

optional arguments:
  -h, --help            show this help message and exit
  -N N                  number of films to show
  -g GENRES, --genres GENRES
                        filter by genres
  -year_from YEAR_FROM  year lower bound filter
  -year_to YEAR_TO      year upper bound filter
  -regexp REGEXP        name of the film filter
  -user USER            username in mysql
  -pswd PSWD            password in mysql
  -host HOST            host name in mysql
  -port PORT            port in mysql
  -db DB                database name
```

## Creating environment

To create environment run setup_environment.py file on the command line with parameters.

## Environment parameters
To get this message use the command from the working directory:
```
python setup_environment.py -h
```
```
usage: setup_environment.py [-h] [-user USER] [-pswd PSWD] [-host HOST]
                            [-port PORT]

optional arguments:
  -h, --help  show this help message and exit
  -user USER  username in mysql
  -pswd PSWD  password in mysql
  -host HOST  host name in mysql
  -port PORT  port in mysql
```


## Examples
### Show top 3 rated movies from 2000 to 2010 in genres (romance, drama, animation) with word death in their titles
```
python main.py -N 3 -year_from 2000 -year_to 2010 -g "Drama|Animation|Romance"
```
![result](https://sun9-57.userapi.com/impg/9dM_G4EcoVOkzfYcBrryuHRQTb7xsOujrROizQ/9nTJgMripqw.jpg?size=867x205&quality=96&sign=531c4446d6293b9bef1179a9fb75b347&type=album)

### Show top 10 movies in genre comedy
```
python main.py -N 10 -g Comedy
```
![result](https://sun9-11.userapi.com/impg/kGGvJNsIgEgyyuJRn0LPHI7etTX_iB9Vkk4iNw/XPJ3l3tjlME.jpg?size=864x223&quality=96&sign=b9a5c1d959128eebf44755bb7f5f55d6&type=album)

### Creating environment by user with name 'root' and password '3110'

```
python setup_environment.py -user root -pswd 3110
```

