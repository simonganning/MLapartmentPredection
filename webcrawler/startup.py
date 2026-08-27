
from seleniumbase import sb_cdp
from playwright.sync_api import sync_playwright




def startup(dates):
    startDate = dates.startDate
    endDate = dates.endDate
    webpage = f"https://www.booli.se/sok/slutpriser?maxSoldDate={endDate}&minSoldDate={startDate}&objectType=L%C3%A4genhet"
    sb = sb_cdp.Chrome(locale="en")
    endpoint_url = sb.get_endpoint_url()
    print(webpage)
   
    p = sync_playwright().start()
    browser = p.chromium.connect_over_cdp(endpoint_url)
    context = browser.contexts[0]
    page = context.pages[0]
    page.goto(webpage)
    sb.sleep(2)
    # an "do you agree" button that always appear
    page.locator("#didomi-notice-agree-button").click()

    return (sb, page, p, webpage)