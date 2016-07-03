import random

from army_factory import ArmyFactory
from constants import STRATEGIES


class Battlefield:
    def __init__(self, num_armies):
        self._armies = []
        for i in range(num_armies):
            self._armies.append(ArmyFactory.create(random.choice(STRATEGIES)))

    def start(self):
        print("There are {} armies. The strategies are:".format(len(self._armies)))
        for i in range(0, len(self._armies)):
            print("{} - {}".format(i, self._armies[i].get_strategy()))
        for i in range(0, len(self._armies)):
            if self._armies[i].is_alive():
                target_army = random.choice([x for x in self._armies if x != self._armies[i] and x.is_alive()])
                print("\tNEW BATTLE army № {} ATTACKS army № {}. It's strategy is {}".format(i, self._armies.index(target_army), self._armies[i].get_strategy()))
                self._armies[i].attack(target_army)

        for i in range(0, len(self._armies)):
            if self._armies[i].is_alive():
                print("ARMY № {} WINS THE WAS. {} IS THE BEST".format(i, self._armies[i].get_strategy()))



