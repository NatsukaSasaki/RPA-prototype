from app.presentation.controllers import controller
from app.application.usecases import usecase
from app.domain.services import service,glugentgate_service
from app.infrastructure.gateways.browser.playwright_gateway import PlaywrightBrowser

def get_controller():
    browser = PlaywrightBrowser()

    ss = service.TestService(browser)
    gs = glugentgate_service.GlugentgateService(browser)
    su = usecase.TestUseCase(ss,gs)
    sc = controller.TestController(su)
    return sc
