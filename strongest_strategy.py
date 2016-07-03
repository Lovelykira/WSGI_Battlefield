from abstract_strategy import AbstractStrategy


class StrongestStrategy(AbstractStrategy):
    @classmethod
    def chose_squad(cls, enemy_army):
        strongest_hp_power = 0
        squad_hp_power = 0
        strongest_squad = 0
        for squad in enemy_army.get_alive_squads():
            for unit in squad.get_alive_units():
                squad_hp_power += unit.get_health() + unit.get_power()
            if squad_hp_power > strongest_hp_power:
                strongest_squad = squad
            squad_hp_power = 0
        return strongest_squad