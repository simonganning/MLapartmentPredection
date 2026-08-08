
from postgreSQL_DB.Batch import Batch
from postgreSQL_DB import setupDatabase as database


def addObjectToDB(dataPoints):
    

    return True


def isObjectInDB(objectID):
    connection = database.connectToDB()
    query = connection.cursor()

    query.execute("""--sql
            SELECT objectID
            FROM listings
            WHERE objectID = {objectID};
        """)

    objectInDatabase = query.fetchone()
    if objectInDatabase is not None:
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


getBatchDates()