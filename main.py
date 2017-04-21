from webcrawl import completeLinks, video_details
import db_insert


def search_aqu():
    search_querie = input("Input keywords for youtube search: ")
    links = completeLinks(search_querie)
    for link in links:
        info = video_details(link)
        db_insert.insertRecords('root', 'music', info['title'],
                                search_querie, info['duration'],
                                info['channel'], info['views'],
                                info['rating'], 0, info['length'],
                                link)
'''
def search_aquisition():
    search_queries = input("Input keywords for youtube search : ")
    links = completeLinks(search_queries)

    db_insert.insertRecords('root', 'music', 'tytul_dorobic', search_queries,
                            3, 0)
'''

if __name__ == '__main__':
    search_aqu()
