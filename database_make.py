import os, sys
import csv
import mysql.connector

global local_path
global source
global conn


def define_value():
    global local_path
    global source
    global conn
    local_path = os.getcwd()
    source = 'bikesharing\\hour.csv'
    conn = None

def query_executor(cursor, param1, param2):
    del_sql = "drop table base_test"
    sql = "create table base_test(instant int(8), dteday DATE, season int(8), yr int(8), mnth int(8), hr int(8), holiday int(8), weekday int(8),workingday int(8),weathersit int(8), temp float(16),atemp float(16),hum float(16), windspeed float(16), casual int(8), registered int(8), cnt int(8))"
    sql_insert = "insert into base_test (instant, dteday, season, yr, mnth, hr, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual, registered, cnt)"
    with open(local_path + '\\' + source, 'r') as R:
        iterator = csv.DictReader(R)
        for n, row in enumerate(iterator):
           get_value = ""
           for key in row.keys():
               if key != 'instant':
                   get_value = get_value + ','
               get_value = get_value + row[key]
           cursor.execute(sql_insert, (get_value))



    #cursor.execute(del_sql)
    #cursor.execute(sql)


if __name__ == "__main__":
    define_value()
    try:
        conn = mysql.connector.connect(host='localhost', port='5934', user='root', password='jemuras1010!',
                                       database='hello_world')

        curs = conn.cursor(dictionary=True)
        query_executor(curs, 'hello', 'world')

        for row in curs:
            print("price is {0}".format(row['price']))


        conn.close()

    except Exception as e:
        print(e.message)

    finally:
        if conn is not None:
            conn.close()
