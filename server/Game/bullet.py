from abc import ABC, abstractmethod

class Bullet(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass