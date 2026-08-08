import psycopg2

def connectToDB():
    connection = psycopg2.connect(host = "localhost", dbname = "postgres" , user = "postgres" , 
                                  password = "1234" , port = 5432)
    return connection
