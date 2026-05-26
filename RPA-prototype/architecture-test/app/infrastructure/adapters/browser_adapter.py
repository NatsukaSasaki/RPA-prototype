from abc import ABC, abstractmethod

class BrowserAdapter(ABC):

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def poweregg_login(self, url: str):
        pass
    @abstractmethod
    def glogent_gate_login(self, url: str):
        pass
    @abstractmethod
    def get_user_id(self):
        pass
    @abstractmethod
    def update_password(self):
        pass
    @abstractmethod
    def status_complete(self):
        pass
    @abstractmethod
    def close(self):
        pass