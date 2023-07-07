
class Logger:
    def __init__(self):
        self.log_index = 0
    
    def log(self, msg):
        self.log_index += 1
        print("Log [%d]: %s" % (self.log_index, msg))

    def reset_log_index(self):
        self.log_index = 0