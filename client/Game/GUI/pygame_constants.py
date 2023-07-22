


PLAYER_SPRITE = [
            0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0, 0,
            0, 0, 1, 1, 0, 1, 1, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0,
            1, 1, 1, 0, 0, 0, 1, 1, 1,
            1, 1, 0, 0, 0, 0, 0, 1, 1,
        ]
PLAYER_SPRITE_SIZE = (9, 9)

BG_COLOR = (0, 0, 0)
GRID_SIZE = 150

PAD_TOP = 40
PAD_LEFT = 10
PAD_RIGHT = 10
PAD_BOTTOM = 10

GRID_LINE_COLOR = (255, 0, 0)

CELL_SIZE = 5
CELL_COLOR = (10, 60, 130)
LINE_WIDTH = 1


# size of each eadge of the screen will be:
# amount of cells * (size of each cell + line width) + padding (from ראשית הצירים)
SCREEN_WIDTH = GRID_SIZE*(CELL_SIZE + LINE_WIDTH) + PAD_LEFT + PAD_RIGHT
SCREEN_HEIGHT = GRID_SIZE*(CELL_SIZE + LINE_WIDTH) + PAD_TOP + PAD_BOTTOM