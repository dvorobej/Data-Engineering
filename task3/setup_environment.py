# -*- coding: utf-8 -*-
"""
Version 1.1

@author: Dmitry Vorobey
"""

import mysql.connector
import argparse
import os


def get_command_arguments():
    """
    Get the arguments from the command line.

        Return value:
            command_args (argparse.Namespace): arguments of the command line
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-user", default="root", type=str, help="username in mysql")
    parser.add_argument("-pswd", default="3110", type=str, help="password in mysql")
    parser.add_argument(
        "-host", default="localhost", type=str, help="host name in mysql"
    )
    parser.add_argument("-port", default="3306", type=str, help="port in mysql")

    command_args = parser.parse_args()

    return command_args


def get_sql_queries(query):
    """
    Get clean sql queries.
    
        Params:
            query (str): string with all queries
        
        Return value:
            clean_queries (list): list of queries
    """
    clean_query = query.replace('$$',';').replace('DELIMITER ;','')
    queries = clean_query.split('\n\n')
    clean_queries = []
    for query in queries:
        if query != '\n':
            clean_queries.append(query)
            
    return clean_queries


def set_environment():
    """
    Create databases, tables, load data into them, create stored procedures.
    
        Return value:
            None
    
    """
    command_args = get_command_arguments()
    # connect to mysql
    try:
        mydb = mysql.connector.connect(
            host=command_args.host,
            port=command_args.port,
            user=command_args.user,
            passwd=command_args.pswd
        )
        
        cursor = mydb.cursor()
    except Exception as e:
        print(e)
        return None
    
    sql_dir_paths = ['db/DDL/Databases',
                 'db/DDL/Tables',
                 'db/DDL/Procedures',
                 'db/DML/Filling_tables/stage_movies_db',
                 'db/DML/Filling_tables/movies_db']
    # read files and execute queries
    for path in sql_dir_paths:
        try:
            for root, dirs, files in os.walk(path,topdown = False):
                for file in files:
                    try:
                        with open(os.path.join(root, file)) as f:
                            query = f.read()
                            queries = get_sql_queries(query)
                            for q in queries:
                                try:
                                    list(cursor.execute(q, multi=True))
                                    mydb.commit()
                                except:
                                    continue
                    except Exception as e:
                        print(e)
                        return None
        except Exception as e:
            print(e)
            return None          
        
    # close conection
    try:
        cursor.close()
        mydb.close() 
    except Exception as e:
        print(e)
        return None
        
    
if __name__ == '__main__':
    set_environment()
    