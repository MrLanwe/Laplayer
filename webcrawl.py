import urllib.request
import urllib.parse
import re
import pafy


def surfWeb(keywords):
    addr_page1 = 'http://www.youtube.com/results?sp=EgIQAQ%253D%253D&'
    addr_page2 = 'http://www.youtube.com/results?sp=EgIQAUgU6gMA&'
    query_string = urllib.parse.urlencode({'search_query': keywords})

    with urllib.request.urlopen(addr_page1 + query_string) as response:
        html = response.read()

    print(query_string)
    search_result = re.findall(r'href=\"\/watch\?v=(.{11})',
                               html.decode())

    return list(set(search_result))


def completeLinks(keywords):
    movies = surfWeb(keywords)

    movie_addr = "http://www.youtube.com/watch?v="

    # print(movies)

    playlist = [movie_addr + movie for movie in movies]

    print(playlist)
    return playlist


def video_details(link):
    vid = pafy.new(link)
    info = {'title': vid.title,
            'duration': vid.duration,
            'length': vid.length,
            'views': vid.viewcount,
            'channel': vid.username,
            'rating': vid.rating}
    return info


def source_code(link):
    with urllib.request.urlopen(link) as sc:
        source = sc.read()
    return source


if __name__ == "__main__":
    search = input("input searched keywords : ")
    completeLinks(search)
