import pymysql
import os
from time import sleep
from getpass import getpass
from queue import Queue


q = Queue()
pl = []


def create_playlist():
    passwd = getpass()
    with pymysql.connect(user='root', db='music', passwd=passwd) as cur:
        cur.execute('SELECT LINK FROM LANWE')
        result = cur.fetchall()
        for link in result:
            q.put(link)
            pl.append(link)


def play_music():
    try:
        while not q.empty():
            os.system('mpv %s --no-video' % q.get())
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        print('exiting')

if __name__ == '__main__':
    create_playlist()
    play_music()
