from client.Game.GUI.gamegui import GameGui

class Game():
    def __init__(self) -> None:
        self.gui = GameGui()

    def Run(self):
        while True:
            self.gui.update([[0 for i in range(150)] for j in range(150)])

if __name__ == "__main__":
    g = Game()
    g.Run()