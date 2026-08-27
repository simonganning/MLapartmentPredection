# Much of the code is based on the links below
# https://github.com/seleniumbase/SeleniumBase/blob/master/examples/cdp_mode/playwright/ReadMe.md
# https://playwright.dev/docs/api/class-locator
from postgreSQL_DB import databaseActions as action


from process import collectData


def main():
    collectData.getData()
    # investigate data 
    # create test set 
    # train models xyz
    # get how bad / good they are
    # if we have already trained a model we should not train it again!


main()