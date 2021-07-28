import logging

if __name__ == '__main__':
   logging.basicConfig(level=logging.DEBUG)
   logging.log(logging.DEBUG,"This is my first debug code.")
   logging.debug("this is a debug message ")
   logging.info("this is warning ")
   logging.error('this is error message ')
   logging.critical("this is critical message ")

   #logging.basicConfig(fiename='app.log', filename ='a', format='%(name)s - %(levelname)s - %(message)s')
   logger = logging.getLogger()
   fhandler = logging.FileHandler(filename='mylog.log', mode='a')
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   fhandler.setFormatter(formatter)
   logger.addHandler(fhandler)
   logger.setLevel(logging.DEBUG)

   logging.log(logging.DEBUG, "This is my first debug code.")
   logging.debug("this is a debug message ")
   logging.info("this is warning ")
   logging.error('this is error message ')
   logging.critical("this is critical message ")
   logging.warning('This will get logged to a file')
   

