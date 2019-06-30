import logging
import view

from app import app


logging.basicConfig(
    filename="Logging.log",
    filemode="w",
    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")


# код для запуска сервиса
if __name__ == '__main__':
    app.run()
