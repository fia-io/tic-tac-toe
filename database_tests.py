#! /usr/bin/python3

import mysql.connector
import unittest

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.connection = mysql.connector.connect(
            user='mb1a', password='', host='127.0.0.1', database='c9')
        cursor = self.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS test")
        cursor.execute("USE test")
        
        with open('schema.sql', 'r') as f:
            command_list = f.read().split('\n\n')
            for command in command_list:
                cursor.execute(command)

    
    def tearDown(self):
        self.connection.cursor().execute("DROP DATABASE IF EXISTS test")
        self.connection.close()


    def testTestTablesTest(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW TABLES")
        count = 0
        for (table_name,) in cursor:
            count += 1
            print(table_name)
        self.assertEqual(1, count)


if __name__ == '__main__':
    unittest.main()
