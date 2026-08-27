from webcrawler import crawlerActions as crawler
from webcrawler import startup as connectToWebsite
import threading

def startThreads(dates):

    threads = []

    for date in dates:

        thread = threading.Thread(
            target=crawler.runCrawler,
            args=(date,)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()