# Maintain Protocol.
import threading
import socket

from shared.ServerAPI.api_constants import *

def client_handshake(logger, client_socket):

    data_from_server = ""
    while(data_from_server != SYN_ACK):
        # Try to connect to the server and perform handshake.    
        try:
            client_socket.connect((SERVER_IP, SERVER_PORT))
            client_socket.send(SYN_REQ.encode())
    
            data_from_server = client_socket.recv(1024).decode()
            
        except Exception as e:
            logger.log(" * Failed To Create Socket \n" + str(e))
            client_socket = socket.socket()
            client_socket.settimeout(0.5)
            continue
    
    logger.log(" * Handshake completed successfully")
    return client_socket

def server_handshake(client, clients_list):
    timeout = 0
    handshake_data = ""
    # Wait for handshake from client.
    while handshake_data != SYN_REQ:
        try:
            handshake_data = client.GetSocket().recv(1024).decode()
            if(handshake_data != SYN_REQ):
                raise ConnectionError
            client.GetSocket().send(SYN_ACK.encode())

        except Exception as e:
            print(e)
            timeout += 1
            if(timeout > 10):
                print("timeout for SYN " + str(client.GetAddress()))
                remove_client(client, clients_list)
                client.GetSocket().close()

                remove_client(client, clients_list)

                return
            continue



def client_mtn(logger, client_socket):
    """
        Checks if the connection to the server is still alive.
        Sends a MTN request to the server and checks the response.
    """
    try:
        client_socket.send(MAINTAIN_CONNECTION.encode())
        MNTN_recv = client_socket.recv(1024).decode()
        return MNTN_recv == MAINTAIN_OK, None
    
    except Exception as e:
        return False, e


def server_mtn(client):
    pass


def remove_client(client, clients_list):
    for client in clients_list:
        if(client.GetAddress()[0] == client.GetAddress()[0]):
            clients_list.remove(client)
            return