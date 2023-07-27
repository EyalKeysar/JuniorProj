from server.Game.bullet import Bullet

class CommonBullet(Bullet):
    def __init__(self, pos, speed):
        self.speed = speed
        self.pos = pos

    def update(self):
        self.pos[1] += self.speed