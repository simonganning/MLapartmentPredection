
from seleniumbase import sb_cdp
from playwright.sync_api import sync_playwright

sb = sb_cdp.Chrome(locale="en")
endpoint_url = sb.get_endpoint_url()
webpage = "https://www.booli.se/sok/slutpriser?objectType=Lägenhet"


def startup():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(endpoint_url)
        context = browser.contexts[0]
        page = context.pages[0]

        return (sb, page)