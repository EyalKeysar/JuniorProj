
class Logger:
    def __init__(self):
        self.log_num = 0
    
    def log(self, msg):
        self.log_num += 1
        print("Log [%d]: %s" % (self.log_num, msg))