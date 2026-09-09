from webcrawler import crawlerActions as crawler

import threading

def startThreads(dates):

    threads = []
    #for date in dates:
    for date in dates[:1]:

        thread = threading.Thread(
            target=crawler.runCrawler(date),
            args=(date, )
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()