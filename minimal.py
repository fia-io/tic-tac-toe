#! /usr/bin/python3

import mysql.connector

cnx = mysql.connector.connect(user='mb1a', password='',
                              host='127.0.0.1',
                              database='c9')
cursor = cnx.cursor()
cursor.execute("USE c9")
cursor.execute("SHOW TABLES")
for (table_name,) in cursor:
        print(table_name)

cnx.close()

print('Done.')