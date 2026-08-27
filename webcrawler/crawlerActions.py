
from webcrawler import startup
import re
from playwright.sync_api import sync_playwright
from postgreSQL_DB import databaseActions as db
from webcrawler import Listing
from webcrawler import startup as connectToWebsite

keepDigits = r'\D'


def runCrawler(date):

    seleniumBase, page, playwright, webpage = connectToWebsite.startup(date)

    multiScraper(
        seleniumBase,
        page,
        webpage
    )

    seleniumBase.sleep(5)

    playwright.stop()

# this method will scrape all of the pages in a specific time period and terminate when finnished
def multiScraper(seleniumBase, page, webpage):
    #scrape one page
    maxPages = 1000
    #go to the next page
    for i in maxPages:
        #code ....
        scrapePage(seleniumBase, page)
        webpage = webpage + f"&page={i}"
        page.goto(webpage)
    #end when we go to a page and all the listings are done

# this method will scrape a page containing max 35 unique objects
# it will collect all the data in each object and put it in a DB
def scrapePage(seleniumBase, page):
    seleniumBase.sleep(2)
    print("before locator")
    #page.locator("#didomi-notice-agree-button").click()
    print ("after locator")
    seleniumBase.sleep(3)
    listingsOnOnePage = page.locator('[class*="object-card__heading--logo"]').all()
    pageurl = page.url

    print (pageurl)

    testAttribute = page.locator('[class*="heading-5 whitespace-nowrap first-letter:uppercase"]')

    for objects in (listingsOnOnePage):
        objects.click()
        seleniumBase.sleep(2)
        pageurl = page.url
        print (pageurl)

        uniqueID = re.sub(keepDigits , "", pageurl )

        if (db.isObjectInDB(uniqueID)):
            datapoints = getObjectInfo(objects, seleniumBase, page, testAttribute)
            seleniumBase.sleep(2)

            # add it all to the DB
            db.addObjectToDB(datapoints)

        page.go_back()



def getObjectInfo(seleniumBase, testPage):
    
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
