import random

from vehicle import Vehicle
from solder_factory import SolderFactory
from constants import NUM_OPERATORS_RANGE


class VehicleFactory:
    @classmethod
    def create(cls):
        vehicle = Vehicle()
        num_operators = random.choice(NUM_OPERATORS_RANGE)
        for i in range(num_operators):
            vehicle.add_operator((SolderFactory.create()))
        return vehicle