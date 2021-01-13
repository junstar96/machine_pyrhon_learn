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
    global local_path
    del_sql = "drop table base_test"
    sql = "create table base_test(instant int(8), dteday int(8), season int(8), yr int(8), mnth int(8), hr int(8), holiday int(8), weekday int(8),workingday int(8),weathersit int(8), temp float(16),atemp float(16),hum float(16), windspeed float(16), casual int(8), registered int(8), cnt int(8))"
    sql_insert = "insert into base_test values ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16})"
    cursor.execute(del_sql)
    cursor.execute(sql)
    with open(local_path + '\\' + source, 'r') as R:
        iterator = csv.DictReader(R)
        for n, row in enumerate(iterator):
           get_value = []
           for key in row.keys():
               get_value.append(row[key])
           cursor.execute(sql_insert.format(get_value[0],get_value[1],get_value[2],get_value[3],get_value[4],
                                            get_value[5],get_value[6],get_value[7],get_value[8],get_value[9],
                                            get_value[10], get_value[11], get_value[12], get_value[13], get_value[14],
                                            get_value[15], get_value[16]))




    print("success")


if __name__ == "__main__":
    global local_path
    global source
    global conn
    define_value()
    try:
        conn = mysql.connector.connect(host='localhost', port='5934', user='root', password='jemuras1010!',
                                       database='hello_world')

        curs = conn.cursor(dictionary=True)
        query_executor(curs, 'hello', 'world')

        conn.commit()

        for row in curs:
            print("price is {0}".format(row['price']))


        conn.close()

    except Exception as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()
