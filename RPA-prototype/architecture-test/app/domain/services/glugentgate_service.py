from app.infrastructure.adapters.browser_adapter import BrowserAdapter 

class TestService:
    def __init__(self, browser: BrowserAdapter):
        self.browser = browser

    def start(self):
        print("start do_service")
        self.browser.start()

    def set_page(self, page):
        self.browser.change_page(page)


    def glogent_gate_login(self):
        self.browser.goto("http://localhost/architecture-test/app/infrastructure/gateways/browser/login2.html")
        self.browser.click(target="ログイン")

    def search_number(self, input: int):
        self.browser.fill(target="#search_text", input=input)
        self.browser.click(target="検索")

    def update_password(self, password: str):
        self.browser.fill(target="#password", input=password)
        self.browser.click(target="更新")

    def click_status_complete(self):
        self.browser.click(target="詳細")
        self.browser.click(target="完了")

    def close(self):
        self.browser.close()
    
       
       