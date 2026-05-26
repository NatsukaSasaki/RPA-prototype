from app.infrastructure.adapters.browser_adapter import BrowserAdapter 

class TestService:
    def __init__(self, browser: BrowserAdapter):
        self.browser = browser

    def start(self):
        print("start do_service")
        self.browser.start()
    """
    def poweregg_login(self):
        self.browser.poweregg_login("http://localhost/architecture-test/app/infrastructure/gateways/browser/login.html")

    def glogent_gate_login(self):
        self.browser.glogent_gate_login("http://localhost/architecture-test/app/infrastructure/gateways/browser/login2.html")
    
    """
    def login(self, url: str):
        self.browser.login(url)

    def get_user_id(self):
        self.browser.get_user_id()

    def update_password(self, url: str):
        self.browser.update_password(123456)

    def status_complete(self):
        self.browser.status_complete()

    def search(self):
        self.browser.search()

    def close(self):
        self.browser.close()

    """
    def do_service(self):
        print("start do_service")
        self.browser.start()
        self.browser.open("https://www.google.com/")
        self.browser.search()
        self.browser.close()
    """

    
       
       