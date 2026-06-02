from app.domain.protocols import protocol

class TestUseCase():

    def __init__(self, test_service: TestProtocol,glugentgate_service: TestProtocol):
        self.test_service = test_service
        self.glugentgate_service = glugentgate_service
        print(type(self.test_service))


    def do_service(self):
        poeweegg_page = self.test_service.start()
        self.test_service.setup_browser()

        self.test_service.poweregg_goto()
        self.test_service.login()
        user_id = self.test_service.get_user_id()

        glugentgate_page = self.glugentgate_service.create_page()
        self.test_service.change_page(glugentgate_page)
        self.glugentgate_service.glugentgate_goto()
        self.glugentgate_service.login()
        self.glugentgate_service.search_number(user_id)
        self.glugentgate_service.update_password("Ncb019011")
        self.test_service.change_page(poeweegg_page)
        self.test_service.click_status_complete()
        self.test_service.close()