from app.presentation.controllers import controller
from app.application.usecases import usecase
from app.domain.services import service
from app.infrastructure.gateways.browser.playwright_gateway import PlaywrightBrowser

def get_controller():
    browser = PlaywrightBrowser()

    ss = service.TestService(browser)
    su = usecase.TestUseCase(ss)
    sc = controller.TestController(su)
    return sc
