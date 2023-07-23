from server.Game.shoot import shoot

class normal_shoot(shoot):
    def __init__(self):
        self.speed = 1
        self.pos = [0,0]

    def update(self):
        self.pos[1] += self.speed