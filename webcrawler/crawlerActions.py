
from webcrawler import startup
import re
from playwright.sync_api import sync_playwright
from postgreSQL_DB import databaseActions as db
from webcrawler import Listing

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
    # adress <h1 class="heading-3 sm:heading-2 mt-4">Tornslingan 43</h1>
    # area and municpal <span class="text-sm text-content-secondary mt-2">Lägenhet · Trångsund · Huddinge</span>
    # proce <span class="heading-2">1&nbsp;825&nbsp;000&nbsp;kr</span>
    # for much else <div class="article-typography"><p>Den har <strong>4&nbsp;647</strong> kr/mån i avgift</p>

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
    
    object = Listing()
    object.livingAreaSqM = livingArea = testPage.nth(0).inner_text()
    rooms = testPage.nth(1).inner_text()
    pricePerSquareMeter = testPage.nth(2).inner_text()
    builtYear = testPage.nth(3).inner_text()



    print( re.sub(keepDigits , "", livingArea ))
    print( re.sub(keepDigits , "",  rooms))
    print( re.sub(keepDigits , "", pricePerSquareMeter ))
    print( re.sub(keepDigits , "", builtYear ))


    return object

    seleniumBase.sleep(10)
