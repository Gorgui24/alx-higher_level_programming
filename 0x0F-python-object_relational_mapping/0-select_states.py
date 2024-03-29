#!/usr/bin/python3
# List all states from a given db sorted in ascending order by id
# Username, password, and database names are given as user args
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", argv[1], argv[2], argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
