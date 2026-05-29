from app.infrastructure.adapters.browser_adapter import BrowserAdapter 

class TestService:
    def __init__(self, browser: BrowserAdapter):
        self.browser = browser

    def start(self):
        print("start do_service")
        return self.browser.start()
        
    def setup_browser(self):
        self.browser.setup_browser()

    def change_page(self,page):
        self.browser.change_page(page)

    def poweregg_goto(self):
        self.browser.goto("http://localhost/RPA-prototype/resource/login.html")

    def login(self):
        self.browser.click(target='input[value="ログイン"]')

    def get_user_id(self):
        number = self.browser.get_user_id()
        return number

    def click_status_complete(self):
        self.browser.click(target='input[value="詳細"]')
        self.browser.click(target='input[value="完了"]')

    def close(self):
        self.browser.close()
    
       
       