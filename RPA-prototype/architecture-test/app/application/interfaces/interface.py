from typing import Protocol

class TestInterface(Protocol):
    def do_service(self) -> None:
        ...