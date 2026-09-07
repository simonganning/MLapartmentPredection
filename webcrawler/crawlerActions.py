import re
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
    for i in range(maxPages):
        scrapePage(seleniumBase, page)
        webpage = webpage + f"&page={i}"
        page.goto(webpage)
        # if there are no more pages to scrape we break the loop
        if (page.locator('[class*="object-card__heading--logo"]') is None):
            break
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


    for objects in (listingsOnOnePage):
        objects.click()
        seleniumBase.sleep(2)
        pageurl = page.url
        print (pageurl)

        uniqueID = re.sub(keepDigits , "", pageurl )

        if not (db.isObjectInDB(uniqueID)):
            datapoints = getObjectInfo(page)
            seleniumBase.sleep(2)

            # add it all to the DB
            db.addObjectToDB(datapoints)

        page.go_back()



def getObjectInfo(page):

    # final price
    finalPrice = page.locator("span.heading-2").first.inner_text()
   # finalPrice.strip()
    print(finalPrice)

    # address
    adress = page.locator("h1.heading-3").inner_text()
    print(adress)

    # areaName / municipal — "Lägenhet · Kungsholmen · Stockholm"
    location_parts = page.locator("span.text-content-secondary.mt-2").inner_text().split("·")
    areaName = location_parts[1].strip()
    municipal = location_parts[2].strip()
    print(areaName)
    print(municipal)

    dateSold = page.locator('p:has-text("Såld eller borttagen")').locator('strong').inner_text()
    print(dateSold)    #<div class="article-typography"><p>Slutpriset blev <strong>3&nbsp;200&nbsp;000</strong> kr</p>
    
    # first four in a column
    column = page.locator('[class*="heading-5 whitespace-nowrap first-letter:uppercase"]')

    # first four in a column
    livingAreaSqM = column.nth(0).inner_text()
    # strip 
    print(livingAreaSqM)

    amountOfRooms = column.nth(1).inner_text()
    # strip
    print(amountOfRooms)

    monthlyFee = column.nth(2).inner_text()
    # strip 
    print(monthlyFee)

    yearBuilt = column.nth(3).inner_text()
    # strip
    print(yearBuilt)

    # tags: elevator, balcony, fireplace
    tags = page.locator("ul.flex.flex-wrap.gap-2 li").all_inner_texts()

    elevator = "Hiss" in tags
    print(elevator)

    balcony = "Balkong" in tags
    print(balcony)

    firePlace = "Eldstad" in tags
    print(firePlace)

    listing = Listing(
        finalPrice,
        adress,
        municipal,
        areaName,
        dateSold,
        livingAreaSqM,
        amountOfRooms,
        monthlyFee,
        yearBuilt,
        elevator,
        balcony,
        firePlace
    )

    return listing
