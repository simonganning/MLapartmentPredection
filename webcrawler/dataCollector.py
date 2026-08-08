# Much of the code is based on the links below
# https://github.com/seleniumbase/SeleniumBase/blob/master/examples/cdp_mode/playwright/ReadMe.md
# https://playwright.dev/docs/api/class-locator

from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp
import re
import json
import http
import startup as connectToWebsite

def main():
   # proxyServers = getProxies() toDoLater
   
    seleniumBase , page = connectToWebsite()
    while(True):
        
        # returns two dates (start and end)
        # we will not fetch months already viewed
        # we will return the specific page we were on last and the indexed object
        # 
        dates = getBatchDates()
        startingPage = lastusedPage(dates)
        startingIndex = lastusedIndex(startingPage)

        while(objectOnPage):

            getNextPage()

            while (pageHasNewObject):
                collectPageData()
                objectId = getUniquieObjectId()
                addDataToDb()
                objectCount = goBackToPage()
    

def pageHasNewObject():
    # is there an object on that page we have not collected? 
    return False

def getBatchDates():
    # look into database what the last month we checked was
    # when a month is checked we mark it as cleared
    return True

def objectOnPage():
    # is there still an object on the page we have not viewed
    return False


def getNextPage():
    # when the current page is empty we simply increment to the next page
    return False

    


#TODO
# collect all the datapoints and create a list with a <hash , list <strings> 
# each listing have a unique sold ID in the domain name we can use
# we shoul save everything in a DB ( 1.6 million listings)
# we should not collect same data twice
# need to go to next wep page , remember last web page in DB so we can continue on the next one 
# keep in mind that new listings are added frequently
# we need a pause and we need mulitple proxies 
 # take dates from 2012 -> 2026 june or similar
 #4370100473364613735
 #4480270175107818889
 #4646671000277108806
 #
 #
 # Booli has 35 listings per page and only ever shows 1000 pages max for every filter. So i guess we wanna make sure we get lower then 
 # 1000 pages per filter so we can play around with it a bit i guess
 # its never more then 8/9 k per month and we can maximum get 35000 k so we have a lot of safe space there
 # We then need to put it into a DB and hash the values based maybe on the listing ID since it should be unique and it 
 # will be easy to find inshalla 
 #


    
"""
    if strongDataValue.count() > 0:
        raw_text = strongDataValue.first.inner_text()
        clean_text = re.sub(r"\s+", " ", raw_text).strip()
        results.append(clean_text)
    else:
        results.append(None)

    # Clean up
    clean_text = re.sub(r"\s+", " ", raw_text).strip()
    print(clean_text)

    browser.close()
    with open("data/housingData.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

sb = sb_cdp.Chrome(locale="en")
endpoint_url = sb.get_endpoint_url()
amountOfWebPages = 1000
listingPerPage = 2
keepDigits = r'\D'

dates = []
results = []
testResults = []

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(endpoint_url)
    context = browser.contexts[0]
    page = context.pages[0]
    webpage = "https://www.booli.se/sok/slutpriser?objectType=Lägenhet"
    
    page.goto(webpage)
    sb.sleep(2)
    page.locator("#didomi-notice-agree-button").click()

    sb.sleep(3)
    oneFullPage = page.locator('[class*="object-card__heading--logo"]').all()

   # print(oneFullPage)
    pageurl = page.url
    print(pageurl)

    for pages in (oneFullPage):
        pages.click()
        sb.sleep(2)
        dataPoints = page.locator('[class*="heading-5 whitespace-nowrap first-letter:uppercase"]')
        livingArea = dataPoints.nth(0).inner_text()
        rooms = dataPoints.nth(1).inner_text()
        pricePerSquareMeter = dataPoints.nth(2).inner_text()
        builtYear = dataPoints.nth(3).inner_text()

        print( re.sub(keepDigits , "", livingArea ))
        print( re.sub(keepDigits , "",  rooms))
        print( re.sub(keepDigits , "", pricePerSquareMeter ))
        print( re.sub(keepDigits , "", builtYear ))



        sb.sleep(15)




"""