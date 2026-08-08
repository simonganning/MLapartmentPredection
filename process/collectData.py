from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp
from webcrawler import startup as connectToWebsite
from webcrawler import crawlerActions as crawler
from postgreSQL_DB import databaseActions as action
from postgreSQL_DB import setupDatabase as setup
from postgreSQL_DB import generateTables as makeTables


def getData():
    connection = setup.connectToDB()
    query = connection.cursor()
    makeTables.createListingsTable(connection, query)
    dateBatches = action.getBatchDates()
    test = dateBatches[0]
    seleniumBase , page , playwright , domain = connectToWebsite.startup(test)
    crawler.scrapePage(seleniumBase, page, domain)
    seleniumBase.sleep(5)
    playwright.stop() 
    connection.close()
    query.close()
    
