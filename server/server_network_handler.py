import socket
from server.constants import *
import threading
from shared.ServerAPI.mtnp import *

class ServerNetworkHandler:
    def __init__(self, logger, client_list):
        self.logger = logger
        self.client_list = client_list
        self.is_running = False

        self.threads_list = []

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', SERVER_PORT))

    def run(self):
        self.is_running = True
        self.logger.log(" * Server started running")
        self.server_socket.listen(1)
        
        print("asd")

        while self.is_running:
            self.logger.log(" * Clients list: " + str(self.client_list))
            client, address = self.server_socket.accept()
            if(address[0] in self.client_list):
                self.client_list.remove(address[0])
                client.close()
                continue

            self.logger.log(" * Client connected from %s:%d" % (address[0], address[1]))
            self.client_list.append(address[0])
            
            # Handle the connection.
            client_thread = threading.Thread(target=self.handle_connection, args=(client, address))
            
            try:
                client_thread.start()
                self.threads_list.append(client_thread)
            except Exception as e:
                self.logger.log(" * Failed to run thread \n" + str(e))
    
    def handle_connection(self, client, address):
        timeout = 0
        server_handshake(client, self.logger, address, self.client_list, self.threads_list)

        # Main Loop
        while True:
            try:
                data = client.recv(1024)
            except Exception as e:
                if(e.errno == 10038):
                    data = None
                elif(e.errno == 10054 or e.errno == 10056):
                    if(address[0] in self.client_list):
                        self.client_list.remove(address[0])
                    client.close()
                    return
                else:
                    raise e
                
            if not data:
                self.logger.log(" * Client didnt send things in mtn? from %s:%d" % (address[0], address[1]))
                if(address[0] in self.client_list):
                    self.client_list.remove(address[0])  
                client.close()
                return
            else:
                data = data.decode()
                server_mtn(data, client, self.logger)
            
                
    def kill(self):
        for thread in self.threads_queue:
            thread.join()
        for client in self.client_queue:
            client.close()

        self.server_socket.close()
        self.logger.log(" * Server stopped running")