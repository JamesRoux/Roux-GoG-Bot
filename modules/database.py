import os
import sqlite3
from sqlite3 import Error
import json

json_directory = 'json'

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(connected, create_table_sql):
    try:
        c = connected.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_into_table(connected, create_table_sql):
    try:
        c = connected.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def populate_db(db_file):
    #
    # We need to populate the databse with the json in this directory
    # so we will iterate over all the files, and extract the headers.
    # then create a table based on the json filename and rows based on
    # the headers in that file name, then populate the rows with data
    #
    for filename in os.listdir(json_directory):
        if filename.endswith(".json"):
            data = open(json_directory + "/" + filename)
            data = json.load(data)

            #
            # First thing we do is create the table
            #
            sql_command = "CREATE TABLE IF NOT EXISTS " + os.path.splitext(filename)[0] + " ("
            i = 0
            for header_label in data["headers"]:
                if i == 0:
                    sql_command = sql_command + header_label + " TEXT NOT NULL"
                    i = i + 1
                else:
                    sql_command = sql_command + "," + header_label + " TEXT NOT NULL"
            sql_command = sql_command + " )"

            print("\ns"+sql_command+"\n")

            connected = create_connection("data.db")

            if connected is not None:
                create_table(connected, sql_command)
            else:
                print("Dude you messed something up")


            #
            # Second thing we do is populate the rows
            # This is done by first getting row values of
            # database by using the files headers section,
            # then it iterates through all the elements of
            # the json commiting it to the database as it goes
            #
            # todo: make this faster
            # todo: check for duplicate lines
            #
            for population_data in data:
                sql_command = "INSERT INTO " + os.path.splitext(filename)[0] + "("
                i = 0
                for header_num in data["headers"]:
                    if i > 0:
                        sql_command = sql_command + ","
                    sql_command = sql_command + header_num
                    i = i + 1
                i = 0
                sql_command = sql_command + ") VALUES("
                for data_num in data[str(population_data)]:
                    if i > 0:
                        sql_command = sql_command + ","
                    if str(data[str(population_data)][i]) == "":
                        data_to_use = "NULL"
                    else:
                        data_to_use = str(data[str(population_data)][i])
                    sql_command = sql_command + '\'' + data_to_use + '\''
                    i = i + 1
                i = 0
                sql_command = sql_command + ");"

                print("\ns"+sql_command+"\n")

                connected = create_connection("data.db")

                if connected is not None:
                    insert_into_table(connected, sql_command)
                    connected.commit()
                else:
                    print("Dude you messed something up")

            continue
        else:
            continue

def update_db():
    create_connection("data.db")
    populate_db("data.db")
    return
