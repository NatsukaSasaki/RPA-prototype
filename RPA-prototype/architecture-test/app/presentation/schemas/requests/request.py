

class TestRequest:
    def __init__(self):
        self.is_valid = False

    def validate(self):
        self.is_valid = True
        print("request is valid")
    