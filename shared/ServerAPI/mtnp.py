# Maintain Protocol.
import threading
import socket

from shared.ServerAPI.api_constants import *

def client_handshake(logger, client_socket):

    data_from_server = ""
    while(data_from_server != SYN_ACK):
        # Try to connect to the server and perform handshake.    
        try:
            logger.log(" * Trying to connect to server...")
            client_socket.connect((SERVER_IP, SERVER_PORT))
            client_socket.send(SYN_REQ.encode())
            logger.log(" * Sent SYN request to server")
    
            data_from_server = client_socket.recv(1024).decode()
            logger.log(f" * Received {data_from_server} from server")
            
        except Exception as e:
            logger.log(" * Failed To Create Socket \n" + str(e))
            client_socket = socket.socket()
            client_socket.settimeout(0.5)
            continue
    
    logger.log(" * Handshake completed successfully")
    return client_socket

def server_handshake(client, logger, address, client_list, threads_list):
    timeout = 0
    handshake_data = ""
    # Wait for handshake from client.
    while handshake_data != SYN_REQ:
        try:
            handshake_data = client.recv(1024).decode()

            if(handshake_data != SYN_REQ):
                raise ConnectionError
            
            client.send(SYN_ACK.encode())

        except Exception as e:
            print(e)
            # If handshake failed, close connection.
            timeout += 1
            if(timeout > 10):
                if(address[0] in client_list):
                    client_list.remove(address[0])
                client.close()
                return
    
    logger.log(" * Handshake completed successfully")



def client_mtn(logger, client_socket):
    """
        Checks if the connection to the server is still alive.
        Sends a MTN request to the server and checks the response.
    """
    try:
        client_socket.send(MAINTAIN_CONNECTION.encode())
        MNTN_recv = client_socket.recv(1024).decode()
        logger.log(f" * MTN response: {MNTN_recv == MAINTAIN_OK}")
        return MNTN_recv == MAINTAIN_OK, None
    except Exception as e:
        return False, e

def server_mtn(data, client, logger):
    if(data == MAINTAIN_CONNECTION):
        client.send(MAINTAIN_OK.encode())
