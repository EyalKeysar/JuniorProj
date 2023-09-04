SERVER_PORT = 1112
SERVER_IP = "127.0.0.1"


# Connection Protocol
SYN_REQ = "SYN" # Synchronize Request
SYN_REQ_LEN = 2
SYN_ACK = "ACK" # Synchronize Acknowledged


GET_ACTIVE_PLAYERS = "GAP" # Get Active Players
MAINTAIN_CONNECTION = "MTN" # Maintain Connection
MAINTAIN_OK = "MTNOK" # Maintain Connection OK
# MCP (Maintanance Connection Protocol)

# database constants
PATH_TO_DB = "./database.txt"
PASSWORD_MIN_LENGTH = 8

PLAYER_START_POS = [10, 100]

# Register 
INVALID_CHARACTERS = [";", "'", ":", ",", " ", "/", "\t", "\r", "\n"]
PASSWORD_MIN_LENGTH = 5


LOGIN_REQUEST = "LGNREQ"
LOGIN_TRUE = "LGNTRUE"

AUTH_REQUEST = "AUTHREQ"
AUTH_TRUE = "AUTHTRUE"
AUTH_FALSE = "AUTHFALSE"


# Game
MOVE_LEFT = "MVL"
MOVE_RIGHT = "MVR"
MOVE_FALSE = "MVFALSE"
SHOOT = "SHOOT"
GET_UPDATES = "GUPD"