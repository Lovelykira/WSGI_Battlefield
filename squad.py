class Squad:
    def __init__(self):
        self._units = []

    def attack(self):
        power = 0
        for unit in self._units:
            if unit.can_attack():
                power += unit.do_attack()
        return power

    def take_damage(self, dmg):
        num_alive_units = len(self.get_alive_units())
        dmg_per_alive_unit = dmg / num_alive_units
        for unit in self.get_alive_units():
            unit.take_damage(dmg_per_alive_unit)

    def is_alive(self):
        for unit in self._units:
            if unit.is_alive():
                return True
        return False

    def get_alive_units(self):
        alive_units = []
        for unit in self._units:
            if unit.is_alive():
                alive_units.append(unit)
        return alive_units

    def recharge(self):
        for unit in self._units:
            if unit.can_attack():
                return False
        else:
            return True

    def add_unit(self, unit):
        self._units.append(unit)

    def __str__(self):
        units = self.get_alive_units()
        units = '\n'.join([str(unit) for unit in units])
        return 'Squad with {} units: \n{}'.format(len(self.get_alive_units()), units)

