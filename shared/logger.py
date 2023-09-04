
class Logger:
    def __init__(self):
        self.log_index = 0
        self.last_msg = ""
    
    def log(self, msg):
        # if(msg != self.last_msg):
        #     self.log_index += 1
        #     self.last_msg = msg
        #     print("Log [%d]: %s" % (self.log_index, msg))
        
        self.log_index += 1
        self.last_msg = msg
        print("Log [%d]: %s" % (self.log_index, msg))


    def reset_log_index(self):
        self.log_index = 0