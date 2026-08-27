
from webcrawler import startup
import re
from playwright.sync_api import sync_playwright
from postgreSQL_DB import databaseActions as db
from webcrawler import Listing
from webcrawler import startup as connectToWebsite

keepDigits = r'\D'


def runCrawler(date):

    seleniumBase, page, playwright = connectToWebsite.startup(date)

    multiScraper(
        seleniumBase,
        page,
        date
    )

    seleniumBase.sleep(5)

    playwright.stop()

# this method will scrape all of the pages in a specific time period and terminate when finnished
def multiScraper(seleniumBase, page, date):



    scrapePage(seleniumBase, page)

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
    # adress <h1 class="heading-3 sm:heading-2 mt-4">Tornslingan 43</h1>
    # area and municpal <span class="text-sm text-content-secondary mt-2">Lägenhet · Trångsund · Huddinge</span>
    # proce <span class="heading-2">1&nbsp;825&nbsp;000&nbsp;kr</span>
    # for much else <div class="article-typography"><p>Den har <strong>4&nbsp;647</strong> kr/mån i avgift</p>

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
