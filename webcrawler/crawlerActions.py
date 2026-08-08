
from webcrawler import startup
import re
from playwright.sync_api import sync_playwright
from postgreSQL_DB import databaseActions as db

keepDigits = r'\D'

def scrapePage(seleniumBase, page, domain):
    seleniumBase.sleep(2)
    print("before locator")
    #page.locator("#didomi-notice-agree-button").click()
    print ("after locator")
    seleniumBase.sleep(3)
    oneFullPage = page.locator('[class*="object-card__heading--logo"]').all()
    pageurl = page.url

    print (pageurl)

    testAttribute = page.locator('[class*="heading-5 whitespace-nowrap first-letter:uppercase"]')

    for pages in (oneFullPage):
        pages.click()
        seleniumBase.sleep(2)
        pageurl = page.url
        print (pageurl)

        uniqueID = re.sub(keepDigits , "", pageurl )

        if (db.isObjectInDB(uniqueID)):
            datapoints = getObjectInfo(pages, seleniumBase, page, testAttribute)
            seleniumBase.sleep(2)

            # add it all to the DB
            db.addObjectToDB(datapoints)

        page.go_back()



def getObjectInfo(pages, seleniumBase, page, testPage):
    
    
    livingArea = testPage.nth(0).inner_text()
    rooms = testPage.nth(1).inner_text()
    pricePerSquareMeter = testPage.nth(2).inner_text()
    builtYear = testPage.nth(3).inner_text()

    print( re.sub(keepDigits , "", livingArea ))
    print( re.sub(keepDigits , "",  rooms))
    print( re.sub(keepDigits , "", pricePerSquareMeter ))
    print( re.sub(keepDigits , "", builtYear ))

    seleniumBase.sleep(10)
