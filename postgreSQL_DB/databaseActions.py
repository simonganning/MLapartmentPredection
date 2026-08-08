
import setupDB as databse


def getBatchDates():
    return True




def addObjectToDB():
    return True


def isObjectInDB(objectID):
    connection = databse.connectToDB()
    query = connection.cursor()

    query.execute("""--sql
            SELECT objectID
            FROM listings
            WHERE objectID = {objectID};
        """)

    objectInDatabas = query.fetchall()
    
    connection.commit()
    query.close()
    connection.close()

    if (objectInDatabas != NULL):
        return True 
    else:
        return False 
