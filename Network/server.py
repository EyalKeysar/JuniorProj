import socket
import threading
import time
import sys
import os
import random
from constants import *
sys.path.append('../')
from networks import *
from logger import Logger

class Server:
    def __init__(self, port=SERVER_PORT):
        # Set up socket.
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', SERVER_PORT))
        self.client_queue = []
        self.active_players =[]
        self.threads_queue = []
        
        self.logger = Logger()
        
    
    def run(self):
        self.is_running = True
        self.logger.log(" * Server started running")
        self.server_socket.listen(1)
        
        while self.is_running:
            # Wait for a connection
            client, address = self.server_socket.accept()
            self.logger.log(" * Client connected from %s:%d" % (address[0], address[1]))
            self.client_queue.append(client)
            self.active_players.append(address)
            
            # Handle the connection.
            client_thread = threading.Thread(target=self.handle_connection, args=(client, address))
            
            try:
                client_thread.start()
                self.threads_queue.append(client_thread)
            except Exception as e:
                self.logger.log(" * Failed to run thread \n" + str(e))
        
    def handle_connection(self, client, address):
        timeout = 0
        handshake_data = ""
        # Wait for handshake from client.
        while handshake_data != SYN_REQ:
            try:
                handshake_data = client.recv(1024).decode()
                if(handshake_data != SYN_REQ):
                    raise ConnectionError
                self.logger.log("Sending ack to client")
                client.send("ACK".encode())

            except Exception as e:
                # If handshake failed, close connection.
                timeout += 1
                if(timeout > 10):
                    client.close()
                    self.logger.log(" * Client disconnected from %s:%d\n Internal exception raised: %s" % (address[0], address[1], e))
                    self.client_queue.remove(client)
                    self.active_players.remove(address)
                    self.threads_queue.remove(threading.current_thread())
                    return
        
        
        # Handshake successful, start game.
                
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    self.logger.log(" * Client disconnected from %s:%d" % (address[0], address[1]))
                    self.client_queue.remove(client)
                    self.active_players.remove(address)
                    self.threads_queue.remove(threading.current_thread())
                    return
                if(data.decode() == MAINTAIN_CONNECTION):
                    self.logger.log(" * Client requested MTN")
                    client.send(MAINTAIN_OK.encode())
                elif(data.decode() == GET_ACTIVE_PLAYERS):
                    self.logger.log(" * Client requested GAP")
                    send_active_players(client, self.active_players, self.logger)
                    self.logger.log(" * Sent GAP")

            except Exception as e:
                self.logger.log(" * Client disconnected from %s:%d\n Internal exception raised: %s" % (address[0], address[1], e))
                self.client_queue.remove(client)
                self.active_players.remove(address)
                self.threads_queue.remove(threading.current_thread())
                return
            
                
        
    def kill(self):
        for thread in self.threads_queue:
            thread.join()
        for client in self.client_queue:
            client.close()

        self.server_socket.close()
        self.logger.log(" * Server stopped running")
    

Server().run()