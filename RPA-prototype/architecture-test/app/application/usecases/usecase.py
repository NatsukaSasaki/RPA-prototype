from app.domain.protocols import protocol

class TestUseCase():

    def __init__(self, test_service: TestProtocol,glugentgate_usecase: TestProtocol):
        self.test_service = test_service
        self.glugentgate_usecase = glugentgate_usecase
        print(type(self.test_service))


    def do_service(self):
        self.test_service.start()
        self.test_service.poweregg_login()
        user_id = self.test_service.get_user_id()
        page = self.test_service.add_page("glugentgate")
        self.test_service.change_page(page)
        self.glugentgate_service.search_number(user_id)
        self.glugentgate_service.update_password("Ncb019011")
        self.glugentgate_service.status_complete()
        self.test_service.close()
        self.glugentgate_service.close()