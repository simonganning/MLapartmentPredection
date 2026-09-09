
from postgreSQL_DB.BatchDate import BatchDate 
from postgreSQL_DB import setupDatabase as database
from webcrawler import Listing


def addObjectToDB(listing: Listing):
    #https://docs.mapbox.com/playground/geocoding/
    connection = database.connectToDB()
    query = connection.cursor()
    query.execute("""--sql
        INSERT INTO listings (
            objectId, finalPrice, adress, municipal, areaName, dateSold,
            livingAreaSquareMeter, amountOfRooms, monthlyFee, yearBuilt,
            elevator, balcony, firePlace
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        listing.objectId,
        listing.finalPrice,
        listing.adress,
        listing.municipal,
        listing.areaName,
        listing.dateSold,
        listing.livingAreaSqM,
        listing.amountOfRooms,
        listing.monthlyFee,
        listing.yearBuilt,
        listing.elevator,
        listing.balcony,
        listing.firePlace,
    ))
    


def isObjectInDB(objectID):
    connection = database.connectToDB()
    query = connection.cursor()

    query.execute(f"""
        SELECT objectID
        FROM listings
        WHERE objectID = {objectID};
            """)

    objectInDatabase = query.fetchone()
    if objectInDatabase is not None:
        return True
    else:
        return False


def checkDate(startDate, pageNumber):
    connection = database.connectToDB()
    query = connection.cursor()
    query.execute("""--sql
            UPDATE batchDates
            SET lastPageUsed = %s
            WHERE startDate = %s
        """, (pageNumber, startDate))
    connection.commit()

def getBatchDates():
    connection = database.connectToDB()
    query = connection.cursor()

    query.execute("""--sql
                SELECT startDate, endDate, lastPageUsed, dateChecked
                FROM batchDates;
            """)

    dates = query.fetchall()

    dateObjects = []

    for date in dates:
        batch = BatchDate(
        date[0], date[1], date[2], date[3])

        print(f" current page {batch.lastPageUsed} end date  + {batch.endDate} start date  + {batch.startDate}")

        dateObjects.append(batch)

    # look into database what the last month we checked was
    # when a month is checked we mark it as cleared
    return dateObjects