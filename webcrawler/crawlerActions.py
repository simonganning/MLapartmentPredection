import re
from postgreSQL_DB import databaseActions as db
from webcrawler.Listing import Listing 
from webcrawler import startup as connectToWebsite
from time import sleep

keepDigits = r'\D'


def runCrawler(date):

    # here we should maybe check tthe last used page , update it etc

    seleniumBase, page, playwright, webpage = connectToWebsite.startup(date)
    startPage = date.currentPage

    multiScraper(
        seleniumBase,
        page,
        webpage,
        startPage
    )

    seleniumBase.sleep(5)

    playwright.stop()

# this method will scrape all of the pages in a specific time period and terminate when finnished
def multiScraper(seleniumBase, page, webpage, startpage):
    #scrape one page
    maxPages = 1000 - startpage
    #go to the next page
    for i in range(maxPages):
        scrapePage(seleniumBase, page)
        webpage = webpage
        page.goto(webpage)
        # if there are no more pages to scrape we break the loop
        if (page.locator('[class*="object-card__heading--logo"]') is None):
            break
    #end when we go to a page and all the listings are done

# this method will scrape a page containing max 35 unique objects
# it will collect all the data in each object and put it in a DB
def scrapePage(seleniumBase, page):
    seleniumBase.sleep(3)
    listingsOnOnePage = page.locator('[class*="object-card__heading--logo"]').all()

    for objects in (listingsOnOnePage):
        objects.click()
        getObjectInfo(page)
        sleep(2)
        page.go_back()



def getObjectInfo(page):

    # final price
    finalPriceRaw = page.locator("span.heading-2").first.inner_text()
    finalPrice = re.sub(keepDigits, "", finalPriceRaw )
    #finalPrice.strip()
    print(finalPrice)

    uniqueIDRaw = page.url
    uniqueID = re.sub(keepDigits , "", uniqueIDRaw )
    print(f"uniqueID {uniqueID}")

    if (db.isObjectInDB(uniqueID)):
        return

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
    livingAreaSqMRaw = column.nth(0).inner_text()
    livingAreaSqM = re.sub(keepDigits, "", livingAreaSqMRaw )
    print(livingAreaSqM)

    amountOfRoomsRaw = column.nth(1).inner_text()
    # strip
    amountOfRooms = re.sub(keepDigits, "", amountOfRoomsRaw )
    print(amountOfRooms)

    monthlyFeeRaw = column.nth(2).inner_text()
    # strip 
    monthlyFee = re.sub(keepDigits, "", monthlyFeeRaw )

    print(monthlyFee)

    yearBuiltRaw = column.nth(3).inner_text()
    yearBuilt = re.sub(keepDigits, "", yearBuiltRaw )
    print(yearBuilt)

    # tags: elevator, balcony, fireplace
    tags = page.locator("ul.flex.flex-wrap.gap-2 li").all_inner_texts()

    elevator = "Hiss" in tags
    print(elevator)

    balcony = "Balkong" in tags
    print(balcony)

    firePlace = "Eldstad" in tags
    print(firePlace)

    print (Listing)

    listing = Listing(
        uniqueID,
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
    db.addObjectToDB(listing)

    return listing
