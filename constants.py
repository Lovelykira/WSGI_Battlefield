from random_strategy import RandomStrategy
from weakest_strategy import WeakestStrategy
from strongest_strategy import StrongestStrategy

NUM_SQUADS_RANGE = range(1, 3)
NUM_SOLDERS_RANGE = range(1, 3)
NUM_VEHICLE_RANGE = range(1, 3)
NUM_OPERATORS_RANGE = range(1, 3)
START_SOLDER_EXPERIENCE = 0
MAX_SOLDER_EXPERIENCE = 50
MAX_UNIT_HEALTH = 100
UNIT_RECHARGE_RANGE = (1, 30)
FIRST_ATTACK_TIME = 0.0
STRATEGIES = [RandomStrategy, WeakestStrategy, StrongestStrategy]