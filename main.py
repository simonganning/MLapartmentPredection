# Much of the code is based on the links below
# https://github.com/seleniumbase/SeleniumBase/blob/master/examples/cdp_mode/playwright/ReadMe.md
# https://playwright.dev/docs/api/class-locator


from process import collectData
import threading

def main():
   # proxyServers = getProxies() do this later when we have one IP working
    collectData.getData()

    # assign each thread their own batch so they dont race for the same object


    # while(True):
        
        
    #     startingPage = query.lastusedPage(dates)
    #     startingIndex = query.lastusedIndex(startingPage)



    #     while(objectOnPage):

    #         getNextPage()

    #         while (pageHasNewObject):
    #             collectPageData()
    #             objectId = getUniquieObjectId()
    #             addDataToDb()
    #             objectCount = goBackToPage()
    



    


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




"""

main()