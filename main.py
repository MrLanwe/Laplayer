from webcrawl import completeLinks
import db_insert


def search_aquisition():
    search_queries = input("Input keywords for youtube search : ")
    links = completeLinks(search_queries)

    db_insert.insertRecords('root', 'music', 'tytul_dorobic', search_queries,
                            3, 0)
