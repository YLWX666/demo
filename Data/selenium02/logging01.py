import logging
import os
import time

class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def save_file(self,message):
        file_path = time.strftime('%Y-%m-%d', time.gmtime()) + 'text.log'
        file = os.path.join(os.getcwd(), file_path)
        conse = logging.FileHandler(file,encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(module)s %(funcName)s %(message)s')
        conse.setFormatter(formatter)
        self.logger.addHandler(conse)
        self.logger.debug(message)
        conse.close()
        self.logger.removeHandler(conse)

    def main(self,message):
        self.save_file(message)

if __name__ == '__main__':
    log = Log()
    log.main('你好')


