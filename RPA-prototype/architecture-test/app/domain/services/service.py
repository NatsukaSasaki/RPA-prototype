from app.infrastructure.adapters.browser_adapter import BrowserAdapter 

class TestService:
    def __init__(self, browser: BrowserAdapter):
        self.browser = browser

    def start(self):
        print("start do_service")
        self.browser.start()
    
    def add_page(self,name):
        page =self.browser.add_page(name)
        return page
    
    def change_page(self,name):
        self.browser.change_page(name)

    def poweregg_login(self):
        self.browser.context_goto("http://localhost/architecture-test/app/infrastructure/gateways/browser/login.html")
        
    def get_user_id(self):
        number = self.browser.get_user_id()
        return number

    def close(self):
        self.browser.close()
    
       
       