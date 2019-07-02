from app import app
import view, logging

logging.basicConfig(
    filename="Logging_web.log",
    filemode="w",
    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

if __name__ == '__main__':
    app.run(port=5020)
