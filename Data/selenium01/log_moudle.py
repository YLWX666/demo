import time

class Loginfo():
    def __init__(self,path='',mode='a'):
        fname = path+time.strftime('%Y-%m-%d',time.gmtime())
        self.log = open(fname+'.txt',mode,encoding='utf-8')
    def log_write(self,loginfo):
        self.log.write(loginfo)
    def log_close(self):
        self.log.close()
if __name__ =='__main__':
    log = Loginfo()
    log.log_write('test loginfo测试')
    log.log_close()