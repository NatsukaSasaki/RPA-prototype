from app.presentation.schemas.requests import request
from app.application.interfaces import interface

class TestController:

    def __init__(self, usecase: interface.TestInterface):
        self.usecase = usecase
        print(type(self.usecase))

    def download(self):
        r = request.TestRequest()
        r.validate()

        self.usecase.do_service()