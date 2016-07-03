import random
import time

from unit import Unit


class Vehicle(Unit):
    def __init__(self):
        super().__init__()
        self._operators = []

    def do_attack(self):
        self._next_attack_time = time.time() + self._recharge
        return self.get_power()

    def take_damage(self, dmg):
        veh_dmg = dmg * 0.6
        self._armor = self.calc_armor()
        if self._armor < veh_dmg:
            self._health = self._health - veh_dmg + self._armor
        random_operator_dmg = dmg * 0.2
        random_operator = random.choice(self._operators)
        random_operator.take_damage(random_operator_dmg)
        for operator in self._operators:
            if operator != random_operator:
                operator.take_damage(dmg * 0.1)

    def calc_armor(self):
        operators_sum_exp = 0
        for operator in self._operators:
            operators_sum_exp += operator.get_experience() / 100
        return 0.1 + operators_sum_exp

    def add_operator(self, operator):
        self._operators.append(operator)

    def get_power(self):
        op_sum_attack = 0
        for operator in self._operators:
            op_sum_attack += operator.do_attack()
        return 0.5 * (1 + self._health / 100) * op_sum_attack / len(self._operators)
