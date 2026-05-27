from app.domain.protocols import protocol

class TestUseCase():

    def __init__(self, glugentgate_service: TestProtocol):
        self.glugentgate_service = glugentgate_service
        print(type(self.glugentgate_service))


    def glugentgate_do_service(self):
        self.glugentgate_service.start()
        self.glugentgate_service.update_password()
        self.glugentgate_service.status_complete()
        self.glugentgate_service.close()