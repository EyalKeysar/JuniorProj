
from networks import *
from draws import *

class LobbyHandler:
    def __init__(self, screen, client_socket, logger):
        self.screen = screen
        self.client_socket = client_socket
        self.logger = logger
        self.is_connected = True
        self.available_players = []

    def run(self):
        self.logger.log(" * Lobby Handler started running")
        while True:
            try:
                self.is_connected = CheckConnection(self.client_socket)
                active_players = get_active_players(self.client_socket, self.logger)
            except Exception as e:
                self.logger.log(" * Connection to server lost")
                self.is_connected = False

                draw_lobby_screen(self.screen, self.is_connected)

                self.client_socket = HandelConnectionError(e, self.logger, self.client_socket)
                continue

            draw_lobby_screen(self.screen, self.is_connected)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return