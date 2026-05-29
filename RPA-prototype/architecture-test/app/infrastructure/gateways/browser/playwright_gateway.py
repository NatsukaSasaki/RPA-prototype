from playwright.sync_api import sync_playwright
from app.infrastructure.adapters.browser_adapter import BrowserAdapter
import time

class PlaywrightBrowser(BrowserAdapter):


    def __init__(self):
        self.playwright = None
        self.browser = None
        context = None
        self.page = None


    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless = False
            )

        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def setup_browser(self):
        pass

    def create_page(self):
        self.page = self.context.new_page()
        return self.page
      
    def change_page(self, page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def get_user_id(self):
        number = self.page.locator("#staff_number").text_content()
        return number

    def click(self, target):
        self.page.locator(target).click()

    def fill(self, target:str, input: str):
        self.page.locator(target).fill(input)
        #locator = self.page.locator("#search_text")
        #print(locator.count()) 

    def close(self):
        print("close")
        self.context.close()
        self.browser.close()
        self.playwright.stop()


"""
        self.pages["main"] = {
            "context": self.context,
            "page": page
        }
        
    def add_page(self, name):
        
        context = self.browser.new_context()

        page = context.new_page()

        self.pages[name] = {
            "context": context,
           " page", page
        }
"""

"""
    def update_password(self, contextno, number: str):
        context = getattr(self,contextno)
        context.locator("input[id=\"serch_text\"]").fill("123456")
"""
   

"""
    def fill_password(self):
        self.context2.locator("input[id=\"password\"]").fill("Ncb019011")


    def click_submit_update(self):
        self.context2.locator("input[type=\"submit\"][value=\"更新\"]").click()


    def click_status_complete(self):
        self.context.locator("input[type=\"submit\"][value=\"詳細\"]").click()
        self.context.locator("input[type=\"submit\"][value=\"完了\"]").click()
"""

   