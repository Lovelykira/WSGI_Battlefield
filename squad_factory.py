import random

from solder_factory import SolderFactory
from vehicle_factory import VehicleFactory
from squad import Squad
from constants import NUM_SOLDERS_RANGE, NUM_VEHICLE_RANGE


class SquadFactory:
    _available_units = {SolderFactory: NUM_SOLDERS_RANGE, VehicleFactory: NUM_VEHICLE_RANGE}

    @classmethod
    def create(cls):
        squad = Squad()
        factories = cls._available_units
        for factory, number in factories.items():
            for i in range(random.choice(number)):
                squad.add_unit(factory.create())
        return squad