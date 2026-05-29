from app.infrastructure.adapters.browser_adapter import BrowserAdapter 

class GlugentgateService:
    def __init__(self, browser: BrowserAdapter):
        self.browser = browser

    def start(self):
        print("start do_service")
        page = self.browser.start()
        return page

    def create_page(self):
        page = self.browser.create_page()
        return page

    def glugentgate_goto(self):
        self.browser.goto("http://localhost/RPA-prototype/resource/login2.html")

    def login(self):
        self.browser.click(target='input[value="ログイン"]')

    def search_number(self, number: str):
        self.browser.fill(target="#search_text", input=number)
        self.browser.click(target='input[value="検索"]')

    def update_password(self, password: str):
        self.browser.fill(target="#password", input=password)
        self.browser.click(target='input[value="更新"]')

    def close(self):
        self.browser.close()
    
       
       