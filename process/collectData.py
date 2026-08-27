from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp
from webcrawler import startup as connectToWebsite
from webcrawler import crawlerActions as crawler
from webcrawler import threads
from postgreSQL_DB import databaseActions as action
from postgreSQL_DB import setupDatabase as setup
from postgreSQL_DB import generateTables as makeTables
import threading



def getData():
    connection = setup.connectToDB()
    query = connection.cursor()
    makeTables.createListingsTable(connection, query)
    dates = action.getBatchDates()

    threads.startThreads(dates)

    
    connection.close()
    query.close()
    
