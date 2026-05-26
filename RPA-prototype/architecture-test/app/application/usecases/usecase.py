from app.domain.protocols import protocol

class TestUseCase():

    def __init__(self, test_service: TestProtocol):
        self.test_service = test_service
        print(type(self.test_service))


    def do_service(self):
        self.test_service.start()
        #self.test_service.poweregg_login()
        #self.test_service.glogent_gate_login()
        self.test_service.login()
        self.test_service.get_user_id()
        self.test_service.update_password()
        self.test_service.status_complete()
        self.test_service.close()

        #self.test_service.do_service()

        
