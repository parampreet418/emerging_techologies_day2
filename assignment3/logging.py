import logging

logging.basicConfig(filename='logfile.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This program created by parampreet')
logging.info('Info of the program')
logging.warning('Warnings')
logging.error('Errors')
