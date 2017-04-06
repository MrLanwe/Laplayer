from time import sleep
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re


def surfWeb(keywords, i):
    addr = 'http://www.youtube.com/results?sp=EgIQAQ%253D%253D&'
    query_string = urllib.parse.urlencode({'search_query': keywords})

    with urllib.request.urlopen(addr + query_string) as response:
        html = response.read()

    print(query_string)
    search_result = re.findall(r'href=\"\/watch\?v=(.{11})',
                               html.decode())
    movie_addr = "http://www.youtube.com/watch?v=" + search_result[i]
    print(movie_addr)

    return movie_addr

if __name__ == "__main__":
    surfWeb('szukaj test cos (takie)', 3)
