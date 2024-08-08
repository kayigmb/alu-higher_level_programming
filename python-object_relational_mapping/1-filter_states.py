#!/usr/bin/python3
"""
commenting done
"""

from sys import argv

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for i in cursor.fetchall():
        if i[1][0] == "N":
            print(i)
    cursor.close()
    db.close()
