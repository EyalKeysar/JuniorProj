import socket
from server.constants import *
import threading
from shared.ServerAPI.mtnp import *
from server.client import Client
import sys

class ServerNetworkHandler:
    def __init__(self, port):

        self.waiting_for_clients = False

        # Socket server setup
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', port))



    def GetClient(self, client_list):
        self.waiting_for_clients = True # Activate Flag So No Other Thread Can Run This Method until this one is done

        print("Ready to accept a new client")

        self.server_socket.listen(1) # Listen for clients (blocking)

        client_socket, address = self.server_socket.accept()

        print("Accepted a new client from " + str(address) + " on port " + str(address[1]))

        cur_client = Client(client_socket, address)


        # If Client address already used b a user than finish the previues connection.
        for client in client_list:
            if(client.GetAddress()[0] == cur_client.GetAddress()[0]):
                # update client socket and port
                client.SetSocket(client_socket)
                client.SetAddress(address)
                server_handshake(client, client_list) 
                client_list.append(client)
                self.waiting_for_clients = False # Deactivate Flag
                return


        server_handshake(cur_client, client_list)

        client_list.append(cur_client)

        self.waiting_for_clients = False # Deactivate Flag

                
    def kill(self):
        for thread in self.threads_queue:
            thread.join()
        for client in self.client_queue:
            client.close()

        self.server_socket.close()