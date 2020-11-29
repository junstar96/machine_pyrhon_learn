import os, sys
import csv
import mysql.connector

global local_path
global source
global conn
local_path = os.getcwd()
source = 'bikesharing\\hour.csv'
conn = None

def query_executor(cursor, param1, param2):
    sql = "select * from food where name = %s or name = %s ;"
    cursor.execute(sql, (param1, param2))

if __name__ == "__main__":
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
