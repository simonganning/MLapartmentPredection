
from postgreSQL_DB import setupDatabase as database

def createListingsTable(connection , query):
    query.execute("""--sql
            CREATE TABLE IF NOT EXISTS listings (
            objectId INT PRIMARY KEY,
            finalPrice INT,
            adress VARCHAR(100),
            municipal VARCHAR(50),
            areaName VARCHAR(50),
            dateSold VARCHAR(10),
            livingAreaSquareMeter INT,
            amountOfRooms INT,
            monthlyFee INT,
            yearBuilt INT,
            xCordinates INT,
            yCorinates INT,
            elevator BOOLEAN,
            balcony BOOLEAN,
            firePlace BOOLEAN
            );
         """)
    
    query.execute("""--sql
                CREATE TABLE IF NOT EXISTS batchDates (
                startDate VARCHAR(8),
                endDate VARCHAR(8),
                lastPageUsed INT,
                lastObjectUsed INT,
                usedDate BOOLEAN
                );
             """)

    query.execute("""--sql
                SELECT startDate
                FROM batchDates;
            """)
    
    doesDatesExist = query.fetchone() is not None

    if  not doesDatesExist:
        datesList = generateDates()

        for start_date, end_date in datesList:
            query.execute("""
                INSERT INTO batchDates
                    (startDate, endDate, lastPageUsed, lastObjectUsed, usedDate)
                VALUES (%s, %s, %s, %s, %s);
            """, (start_date, end_date, 0, 0, False))
    
    connection.commit()

    rows = printRows(query)

   # for row in rows:
   #         print(row)

    # everything went well no errors
    return True


def generateDates():
    # first date is 20120101
    # last date is 20251231
    # gives us 13 whole years and two half years
    # 28 different batches
    dates = []
    
    for year in range(2012, 2026):
        dates.append((f"{year}0101" , f"{year}0631"))
        dates.append((f"{year}0701" , f"{year}1231"))

    dates.append(("20260101" , "20260731"))
    return dates

def printRows(query):
    query.execute("""--sql
                    SELECT *
                    FROM batchDates;
                """)
    return query.fetchall()