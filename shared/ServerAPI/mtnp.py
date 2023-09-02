# Maintain Protocol.
import threading
import socket

from shared.ServerAPI.api_constants import *

def client_handshake(logger, client_socket):
    """
        Performs a handshake with the server.
        Handeling failed handshakes by restarting the socket and trying again.

        :param logger: The logger object.
        :param client_socket: The socket to perform the handshake with.
        :return: The socket after the handshake.
    """
    print("client handshake called")
    data_from_server = ""
    while(data_from_server != SYN_ACK):
        # Try to connect to the server and perform handshake.    
        try:
            client_socket.connect((SERVER_IP, SERVER_PORT))
            print("connected to server, handshaking")
            client_socket.send(SYN_REQ.encode())
    
            data_from_server = client_socket.recv(1024).decode()
            continue
            
        except Exception as e:
            logger.log(" ! handshake failed, restaeting socket and handshaking again. \n" + str(e))
            client_socket = socket.socket()
            client_socket.settimeout(0.5)
            continue
    
    logger.log(" * Handshake completed successfully")
    return client_socket

def server_handshake(client, clients_list):
    print("server handshake called")
    client.GetSocket().settimeout(2)
    timeout = 0
    handshake_data = ""
    # Wait for handshake from client.
    while handshake_data != SYN_REQ:
        try:
            handshake_data = client.GetSocket().recv(1024).decode()
            if(handshake_data != SYN_REQ):
                print("error in handshake - " + str(handshake_data))
                raise ConnectionError
            client.GetSocket().send(SYN_ACK.encode())

        except Exception as e:
            print(" ---- error in handshake - " + str(e))

            timeout += 1
            if(timeout > 10):
                print("timeout for SYN " + str(client.GetAddress()))
                remove_client(client, clients_list)
                client.GetSocket().close()
                remove_client(client, clients_list)
                return
            continue

    print("handshake completed")
    client.GetSocket().settimeout(2)



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