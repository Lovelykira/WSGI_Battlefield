import random

from army_factory import ArmyFactory
from constants import STRATEGIES


class Battlefield:
    def __init__(self, num_armies):
        self._armies = []
        for i in range(num_armies):
            self._armies.append(ArmyFactory.create(random.choice(STRATEGIES)))

    def start(self):
        res = ""
        res += "There are {} armies.<br> The strategies are:".format(len(self._armies))
        for i in range(0, len(self._armies)):
            res += "<br>{} - {}".format(i, self._armies[i].get_strategy())
        while True:
            for i in range(0, len(self._armies)):
                if self._armies[i].is_alive() and len([x for x in self._armies if x.is_alive()])>1:
                    target_army = random.choice([x for x in self._armies if x != self._armies[i] and x.is_alive()])
                    res += "<br><br>&ensp;NEW BATTLE army # {} ATTACKS army # {}. It's strategy is {}<br>".format(i, self._armies.index(target_army), self._armies[i].get_strategy())
                    res += self._armies[i].attack(target_army)

            if len([x for x in self._armies if x.is_alive()])==1:
                break

        for i in range(0, len(self._armies)):
            if self._armies[i].is_alive():
                res += "<br><br>&ensp;ARMY # {} WINS THE WAR. {} IS THE BEST".format(i, self._armies[i].get_strategy())

        return res



