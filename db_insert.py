#!/usr/bin/python3.4
import pymysql
import datetime


def insertRecords(usr, db, title, keywords, duration, grade):
    ts = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    with pymysql.connect(user=usr, db=db, passwd='aspirinc12', autocommit=True) as cur:
        cur.execute("""INSERT INTO LANWE(TITLE, \
                       KEYWORDS, DURATION, GRADE, TIMESTAMP) \
                       VALUES ('%s', '%s', '%f', '%d', '%s')""" %
                       (title, keywords, duration, grade, ts))


def updateGrade(usr, db, gr):
    with pymysql.connect(user=usr, db=db, passwd='aspirinc12', autocommit=True) as cur:
        cur.execute("UPDATE LANWE SET GRADE=%d" % gr, "WHERE TITLE='tytul tytul'")


if __name__ == "__main__":
    insertRecords('root', 'music', 'tytul tytul', 'keywords', 333, 0)
