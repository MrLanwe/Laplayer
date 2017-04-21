#!/usr/bin/python3.4
import pymysql
import datetime


def insertRecords(usr, db, title, keywords, duration, ch, views,
                  rating, grade, length, link):
    ts = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    with pymysql.connect(user=usr, db=db, passwd='aspirinc12', autocommit=True) as cur:
        cur.execute("""INSERT INTO LANWE(TITLE, \
                       KEYWORDS, DURATION, CHANNEL, VIEWS, RATING, GRADE, \
                       TIMESTAMP, LENGTH, LINK)
                       VALUES ('%s', '%s', '%s', '%s', '%d', '%f', '%d', '%s',
                               '%d', '%s')""" %
                       (title, keywords, duration, ch, views, rating, grade,
                        ts, length, link))


def updateGrade(usr, db, gr):
    with pymysql.connect(user=usr, db=db, passwd='aspirinc12', autocommit=True) as cur:
        cur.execute("UPDATE LANWE SET GRADE=%d" % gr, "WHERE TITLE='tytul tytul'")


if __name__ == "__main__":
    insertRecords('root', 'music', 'tytul tytul', 'keywords', '01:33:23',
                  'dupa', 55454, 3.325, 6546, 0, 'youtube::link')
