from app.infrastructure.adapters.browser_adapter import BrowserAdapter 

class TestService:
    def __init__(self, browser: BrowserAdapter):
        self.browser = browser

    def start(self):
        print("start do_service")
        self.browser.start()

    def poweregg_login(self):
        self.browser.page_goto("http://localhost/architecture-test/app/infrastructure/gateways/browser/login.html")
        self.browser.click_submit_login()
    def glogent_gate_login(self):
        self.browser.page2_goto("http://localhost/architecture-test/app/infrastructure/gateways/browser/login2.html")
        self.browser.click_submit_login()

    def get_user_id(self):
        self.browser.get_user_id()

    def update_password(self, url: str):
        self.browser.update_password(123456)
        self.browser.click_submit_search()
        self.browser.fill_password()
        self.browser.click_submit_update()

    def click_status_complete(self):
        self.browser.status_complete()

    def close(self):
        self.browser.close()
    
       
       