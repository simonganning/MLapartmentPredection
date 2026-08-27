
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

    #testAttribute = page.locator('[class*="heading-5 whitespace-nowrap first-letter:uppercase"]')

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
    
    object = Listing()

    # other info about the listing
    # outer <div class="flex flex-col justify-center items-start mt-1"><p><span class="text-sm text-content-secondary">Slutpris</span><button type="button" class="inline align-sub text-sm ml-2 " aria-label="Visa mer info" aria-haspopup="true" aria-controls="_r_8_" aria-expanded="false"><svg class="h-4 w-4" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M10 20C15.5228 20 20 15.5228 20 10C20 4.47715 15.5228 0 10 0C4.47715 0 0 4.47715 0 10C0 15.5228 4.47715 20 10 20ZM11.1545 12.5136H8.98374V12.0529C8.98374 11.0443 9.46341 10.2502 10.1138 9.67836L10.9837 8.92389C11.561 8.4315 11.7967 7.97882 11.7967 7.53408C11.7967 6.38253 11.0894 5.91396 10.0406 5.91396C8.93496 5.91396 8.29268 6.64461 8.17073 7.55791H6C6.1626 5.3501 7.79675 4 10.0569 4C12.1789 4 14 5.14361 14 7.56585C14 8.49504 13.3496 9.28921 12.5203 9.94044L11.8699 10.4487C11.3496 10.8855 11.1545 11.5923 11.1545 12.45V12.5136ZM11.5854 14.634C11.5854 15.3647 10.9431 16 10.1707 16C9.37398 16 8.76423 15.3647 8.76423 14.634C8.76423 13.9034 9.37398 13.2998 10.1707 13.2998C10.9431 13.2998 11.5854 13.9034 11.5854 14.634Z" fill="currentColor"></path></svg></button></p><div class="flex items-center"><div class="bg-content-warning w-1 md:w-2 h-10 mr-2 rounded-xs"></div><span class="heading-2">6&nbsp;750&nbsp;000&nbsp;kr</span></div></div>
    #inner <span class="heading-2">6&nbsp;750&nbsp;000&nbsp;kr</span>
    object.finalPrice

    # adress
    object.adress
    #<h1 class="heading-3 sm:heading-2 mt-4">Rålambsvägen 12</h1>
    
    #<span class="text-sm text-content-secondary mt-2">Lägenhet · Kungsholmen · Stockholm</span>
    object.areaName
    object.municipal

    # first four in a column
    object.livingAreaSqM = page.nth(0).inner_text()
    object.rooms = page.nth(1).inner_text()
    object.monthlyFee = page.nth(2).inner_text()
    object.builtYear = page.nth(3).inner_text()

    # are all in this class 
    # <ul class="flex flex-wrap gap-2 mt-6"><li><div class="tag tag--light  tag--with-icon tag--large "><span class="tag__icon-container"><div class="svg-icon-mask w-5 h-5 " style="mask-image: url(&quot;https://bcdn.se/assets/shared/icons/ElevatorOutlined.svg&quot;);"></div></span>Hiss</div></li><li><div class="tag tag--light  tag--with-icon tag--large "><span class="tag__icon-container"><div class="svg-icon-mask w-5 h-5 " style="mask-image: url(&quot;https://bcdn.se/assets/shared/icons/BalconyOutlined.svg&quot;);"></div></span>Balkong</div></li><li><div class="tag tag--light  tag--with-icon tag--large "><span class="tag__icon-container"><div class="svg-icon-mask w-5 h-5 " style="mask-image: url(&quot;https://bcdn.se/assets/shared/icons/FireplaceOutlined.svg&quot;);"></div></span>Eldstad</div></li></ul>

    # balcony , fireplace and elevator
    object.elevator
    #<div class="tag tag--light  tag--with-icon tag--large "><span class="tag__icon-container"><div class="svg-icon-mask w-5 h-5 " style="mask-image: url(&quot;https://bcdn.se/assets/shared/icons/ElevatorOutlined.svg&quot;);"></div></span>Hiss</div>    
    object.balcony 
    #<div class="tag tag--light  tag--with-icon tag--large "><span class="tag__icon-container"><div class="svg-icon-mask w-5 h-5 " style="mask-image: url(&quot;https://bcdn.se/assets/shared/icons/BalconyOutlined.svg&quot;);"></div></span>Balkong</div>
    object.firePlace
    #<div class="tag tag--light  tag--with-icon tag--large "><span class="tag__icon-container"><div class="svg-icon-mask w-5 h-5 " style="mask-image: url(&quot;https://bcdn.se/assets/shared/icons/FireplaceOutlined.svg&quot;);"></div></span>Eldstad</div>



    return object
