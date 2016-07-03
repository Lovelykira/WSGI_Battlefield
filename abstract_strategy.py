from abc import ABCMeta, abstractmethod

class AbstractStrategy(metaclass=ABCMeta):
    @abstractmethod
    def chose_squad(cls, enemy_army):
        pass