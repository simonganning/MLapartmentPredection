
from webcrawler import startup
import re
from playwright.sync_api import sync_playwright

def scrapePage(seleniumBase, page, domain):
    seleniumBase.sleep(2)
    print("before locator")
    #page.locator("#didomi-notice-agree-button").click()
    print ("after locator")
    seleniumBase.sleep(3)
    oneFullPage = page.locator('[class*="object-card__heading--logo"]').all()
    pageurl = page.url

    print (pageurl)

    testPage = page.locator('[class*="heading-5 whitespace-nowrap first-letter:uppercase"]')

    for pages in (oneFullPage):
        pages.click()
        seleniumBase.sleep(2)
        datapoints = getObjectInfo(pages, seleniumBase, page, testPage)
        seleniumBase.sleep(2)
        page.go_back()



def getObjectInfo(pages, seleniumBase, page, testPage):
    keepDigits = r'\D'
    
    livingArea = testPage.nth(0).inner_text()
    rooms = testPage.nth(1).inner_text()
    pricePerSquareMeter = testPage.nth(2).inner_text()
    builtYear = testPage.nth(3).inner_text()

    print( re.sub(keepDigits , "", livingArea ))
    print( re.sub(keepDigits , "",  rooms))
    print( re.sub(keepDigits , "", pricePerSquareMeter ))
    print( re.sub(keepDigits , "", builtYear ))

    seleniumBase.sleep(10)
