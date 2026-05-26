from app.infrastructure.logger import logger
from app.cmd import di

logger.info("Start")

def main():
    controller = di.get_controller()
    controller.download()

if __name__ == "__main__":
    main()
    
