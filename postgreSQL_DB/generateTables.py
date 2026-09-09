
def createListingsTable(connection , query):

    query.execute("""--sql
                DROP TABLE IF EXISTS listings
                ;
             """)

    query.execute("""--sql
            CREATE TABLE IF NOT EXISTS listings (
            objectId INT PRIMARY KEY,
            finalPrice INT,
            adress VARCHAR(255),
            municipal VARCHAR(255),
            areaName VARCHAR(255),
            dateSold VARCHAR(255),
            livingAreaSquareMeter INT,
            amountOfRooms INT,
            monthlyFee INT,
            yearBuilt INT,
            elevator BOOLEAN,
            balcony BOOLEAN,
            firePlace BOOLEAN
            );
         """)

    query.execute("""--sql
                    DROP TABLE IF EXISTS batchDates
                    ;
                 """)
    
    query.execute("""--sql
                CREATE TABLE IF NOT EXISTS batchDates (
                startDate VARCHAR(10),
                endDate VARCHAR(10),
                lastPageUsed INT ,
                dateChecked BOOLEAN
                );
             """)

    query.execute("""--sql
                SELECT startDate
                FROM batchDates;
            """)
    
    doesDatesExist = query.fetchone() is not None

    if not doesDatesExist:
        datesList = generateDates()

        for start_date, end_date in datesList:
            query.execute("""
                INSERT INTO batchDates
                    (startDate, endDate, lastPageUsed, dateChecked)
                VALUES (%s, %s, %s, %s);
            """, (start_date, end_date, 0, False))
    
    connection.commit()

    return True


def generateDates():
   
    dates = [
        ("2024-01-01", "2024-03-31"),
        ("2024-04-01", "2024-06-30"),
        ("2024-07-01", "2024-09-30"),
        ("2024-10-01", "2024-12-31"),
        ("2025-01-01", "2025-03-31"),
        ("2025-04-01", "2025-06-30"),
        ("2025-07-01", "2025-09-30"),
        ("2025-10-01", "2025-12-31"),
        ("2026-01-01", "2026-03-31"),
        ("2026-04-01", "2026-06-30"),
        ("2026-07-01", "2026-08-31")
        ]
    
    return dates