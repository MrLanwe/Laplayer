#!/usr/bin/python3.4
import pymysql


def dbTable():
    # Open database connection
    db = pymysql.connect("localhost", "root", "aspirinc12", "music")

    # prepear a cursor object
    c = db.cursor()

    # drop table if it already exist using execute() method
    c.execute("DROP TABLE IF EXISTS LANWE")

    # Create table as per requirements
    sql = """CREATE TABLE LANWE (
             TITLE    CHAR(40)    NOT NULL,
             KEYWORDS    CHAR(40)    NOT NULL,
             DURATION    FLOAT, GRADE    INT,
             TIMESTAMP    DATETIME,
             PLAYTIME    TIMESTAMP)"""

    c.execute(sql)

    # disconnect from server
    db.close()

if __name__ == "__main__":
    dbTable()
