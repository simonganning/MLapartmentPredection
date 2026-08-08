import psycopg2



def connectToDB():
    connection = psycopg2.connect(host = "localhost", dbname = "postgres" , user = "postgres" , 
                                  password = "1234" , port = 5432)
    return connection


def doSome():
    connection = connectToDB()
    cursor = connection.cursor()

    cursor.execute("""--sql
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

    cursor.execute("""--sql
        INSERT INTO listings (
            objectId,
            finalPrice,
            adress,
            municipal,
            areaName,
            dateSold,
            livingAreaSquareMeter,
            amountOfRooms,
            monthlyFee,
            yearBuilt,
            xCordinates,
            yCorinates,
            elevator,
            balcony,
            firePlace
        )
        VALUES
        (
            1001,
            3450000,
            'Storg 1',
            'Stockholm',
            'Södermalm',
            '2026-08-01',
            78,
            3,
            4200,
            1998,
            6589123,
            1623456,
            TRUE,
            TRUE,
            FALSE
        ),
        (
            1002,
            2195000,
            'Parkv2',
            'Uppsala',
            'Luthagen',
            '2026-07-18',
            54,
            2,
            3150,
            1976,
            6645321,
            1598765,
            FALSE,
            TRUE,
            TRUE
        );
    """)

    cursor.execute("""--sql
        SELECT adress
        FROM listings
        WHERE finalPrice > 0;
    """)

    rows = cursor.fetchall()
    print(rows)

    connection.commit()

    # close everything
    cursor.close()
    connection.close()

doSome()