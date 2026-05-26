from playwright.sync_api import sync_playwright
from app.infrastructure.adapters.browser_adapter import BrowserAdapter
import time

class PlaywrightBrowser(BrowserAdapter):

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.context2 = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()
        self.context = self.playwright.chromium.launch(headless = False)
        self.context2 = self.playwright.chromium.launch(headless = False)

"""
    def poweregg_login(self, url: str):
        self.page = self.context.new_page()
        self.page.goto(url)
        self.page.locator("input[type=\"submit\"][value=\"ログイン\"]").click()

    def glogent_gate_login(self, url: str):
        self.page2 = self.context2.new_page()
        self.page2.goto(url)
        self.page2.locator("input[type=\"submit\"][value=\"ログイン\"]").click()
"""
    def login(self, url: str):
        self.page = self.context2.new_page()
        self.page.goto(url)
        self.page.locator("input[type=\"submit\"][value=\"ログイン\"]").click()

    def get_user_id(self):
        number = self.page.locator("tr").locator("td").nth(1).text_content()
        #return number

    def update_password(self, number: str):
        self.page2.locator("input[id=\"serch_text\"]").fill("123456")
        self.page2.locator("input[type=\"submit\"][value=\"検索\"]").click()
        self.page2.locator("input[id=\"password\"]").fill("Ncb019011")
        self.page2.locator("input[type=\"submit\"][value=\"更新\"]").click()

    def status_complete(self):
        self.page.locator("input[type=\"submit\"][value=\"詳細\"]").click()
        self.page.locator("input[type=\"submit\"][value=\"完了\"]").click()

    def close(self):
        print("close")
        self.context.close()