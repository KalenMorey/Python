#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

def dbConnect():
    # Connect to database
    conn = sqlite3.connect('dbFifthElement.db')
    return conn


def dbCreate(conn):
    conn = dbConnect()
    conn.execute("CREATE TABLE if not exists tblRoster( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        colName TEXT, \
        colSpecies TEXT, \
        colIQ INTEGER \
        );")
    dbClose(conn)


def dbPopulate(conn):
    conn = dbConnect()
    conn.execute("INSERT INTO tblRoster (colName, colSpecies, colIQ) VALUES ('Jean-Baptiste Zorg', 'Human',122)")
    conn.execute("INSERT INTO tblRoster (colName, colSpecies, colIQ) VALUES ('Korben Dallas', 'Meat Popsicle', 100)")
    conn.execute("INSERT INTO tblRoster (colName, colSpecies, colIQ) VALUES ('Ak not', 'Mangalor', -5)")
    dbClose(conn)


def dbUpdate(conn):
    conn = dbConnect()
    conn.execute("UPDATE tblRoster SET colSpecies = 'Human' WHERE colName = 'Korben Dallas'")
    dbClose(conn)


def dbShowResult(conn):
    conn = dbConnect()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''SELECT colName, colSpecies, colIQ FROM tblRoster''')
    for row in cursor:
        print('{0} : {1}, {2}'.format(row['colName'], row['colSpecies'], row['colIQ']))
    dbClose(conn)


def dbClose(conn):
    conn.commit()
    conn.close()


def main():
    conn = dbConnect()
    dbCreate(conn)
    dbPopulate(conn)
    dbUpdate(conn)
    dbShowResult(conn)


if __name__ == "__main__":
    main()


    
