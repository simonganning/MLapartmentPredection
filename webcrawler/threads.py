import threading
from postgreSQL_DB import generateTables

def startThreads(dates):
    amountOfThreads = len(dates)

    for threads in amountOfThreads:
        thread = threading.Thread(target=dates[threads])