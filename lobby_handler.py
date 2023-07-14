
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
                self.logger.log(" * Active players: %s" % active_players)
            except Exception as e:
                self.logger.log(" * Connection to server lost")
                self.is_connected = False

                draw_lobby_screen(self.screen, self.is_connected)
                return self.client_socket


            active_players_btn_list = []
            for player in active_players:
                active_players_btn_list.append(Button(ACTPLABTN_COLOR, ACTPLABTN_COLOR_HOVER,
                                                       player, ACTPLABTN_FONT_SIZE, ACTPLABTN_TXT_CLR,
                                                         ACTPLABTN_X, (active_players.index(player) * ACTPLABTN_HEIGHT),
                                                         ACTPLABTN_WIDTH, ACTPLABTN_HEIGHT))


            draw_lobby_screen(self.screen, self.is_connected, active_players_btn_list)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.client_socket