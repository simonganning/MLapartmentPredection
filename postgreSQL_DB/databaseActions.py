
from postgreSQL_DB.Batch import Batch
from postgreSQL_DB import setupDatabase as database


def addObjectToDB():
    return True


def isObjectInDB(objectID):
    connection = database.connectToDB()
    query = connection.cursor()

    query.execute("""--sql
            SELECT objectID
            FROM listings
            WHERE objectID = {objectID};
        """)

    objectInDatabas = query.fetchall()

   # connection.commit()
   # query.close()
   # connection.close()

    if (objectInDatabas != NULL):
        return True 
    else:
        return False 


def pageHasNewObject():
    # is there an object on that page we have not collected? 
    return False

def getBatchDates():
    connection = database.connectToDB()
    query = connection.cursor()

    query.execute("""--sql
                SELECT startDate, endDate, lastPageUsed, lastObjectUsed
                FROM batchDates
                WHERE usedDate = FALSE;
            """)

    dates = query.fetchall()

    dateObjects = []

    #print(dates)

    for date in dates:
        batch = Batch(
        date[0], date[1], date[2] , date[3])

        dateObjects.append(batch)

    # look into database what the last month we checked was
    # when a month is checked we mark it as cleared
    return dateObjects

def objectOnPage():
    # is there still an object on the page we have not viewed
    return False


def getNextPage():
    # when the current page is empty we simply increment to the next page
    return False

getBatchDates()