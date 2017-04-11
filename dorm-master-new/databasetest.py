#!/usr/bin/python3
"""
test sqlite3
"""

import sqlite3


def main():
    """
    main
    """
    # connect to database
    conn = sqlite3.connect("db.sqlite3")
    # create cursor
    cursor = conn.cursor()
    # execute command
    t = 2
    i = 3
    cursor.execute("insert into dormdb_dorm (devID,\
                    devName,devStatus,nRelays,relay1,relay2,\
                    relay3,relay4,relay5,time)\
                    values (" + str(t) +
                   "," + str(t) + "," + str(t) + "," + str(t) +
                   "," + str(t)  + "," + str(t) +
                   "," + str(t) + "," + str(t) + "," +
                   str(i) + ", datetime('now','localtime'))")
    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
