from abc import ABCMeta, abstractmethod
import random
import time

from constants import MAX_UNIT_HEALTH, UNIT_RECHARGE_RANGE, FIRST_ATTACK_TIME


class Unit(metaclass=ABCMeta):
    def __init__(self):
        self._health = MAX_UNIT_HEALTH
        self._recharge = random.choice(UNIT_RECHARGE_RANGE)
        self._next_attack_time = FIRST_ATTACK_TIME
        self._armor = 0

    @abstractmethod
    def do_attack(self):
        pass

    @abstractmethod
    def take_damage(self, dmg):
        pass

    @abstractmethod
    def calc_armor(self):
        pass

    @abstractmethod
    def get_power(self):
        pass

    def can_attack(self):
        now = time.time()
        return now >= self._next_attack_time and self.is_alive()

    def is_alive(self):
        return self._health > 0

    def get_health(self):
        return self._health

    def __str__(self):
        return '{} has {} health'.format(self.__class__.__name__,self._health)
