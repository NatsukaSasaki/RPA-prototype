from abc import ABC, abstractmethod

class BrowserAdapter(ABC):

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def setup_browser(self):
        pass
    @abstractmethod
    def setup_browser(self,name):
        pass
    @abstractmethod
    def create_page(self):
        pass
    @abstractmethod
    def change_page(self,name):
        pass
    @abstractmethod
    def goto(self, url: str):
        pass
    @abstractmethod
    def get_user_id(self):
        pass
    @abstractmethod
    def click(self):
        pass
    @abstractmethod
    def fill(self, target, password: str):
        pass
    @abstractmethod
    def close(self):
        pass