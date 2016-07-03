import random

from squad_factory import SquadFactory
from army import Army
from constants import NUM_SQUADS_RANGE


class ArmyFactory:
    __available_groups = {SquadFactory: NUM_SQUADS_RANGE}

    @classmethod
    def create(cls, strategy):
        army = Army(strategy)
        for factory, number in cls.__available_groups.items():
            for i in range(random.choice(number)):
                army.add_group(factory.create())
        return army