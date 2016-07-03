import time
import random

from unit import Unit
from constants import START_SOLDER_EXPERIENCE, MAX_SOLDER_EXPERIENCE


class Solder(Unit):
    def __init__(self):
        super().__init__()
        self._experience = START_SOLDER_EXPERIENCE

    def do_attack(self):
        self._next_attack_time = time.time() + self._recharge
        if self._experience != MAX_SOLDER_EXPERIENCE:
            self._experience += 1

        return self.get_power()

    def take_damage(self, dmg):
        self._armor = self.calc_armor()
        if self._armor < dmg:
            self._health = self._health - dmg + self._armor

    def calc_armor(self):
        return 0.05 + self._experience / 100

    def get_experience(self):
        return self._experience

    def get_power(self):
        return 0.5 * (1 + self._health) * random.randint(50 + self._experience, 100) / 100
