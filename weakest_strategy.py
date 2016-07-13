from abstract_strategy import AbstractStrategy


class WeakestStrategy(AbstractStrategy):
    @classmethod
    def chose_squad(cls, enemy_army):
        weakest_hp = float('inf')
        squad_hp = 0
        weakest_squad = 0
        for squad in enemy_army.get_alive_squads():
            for unit in squad.get_alive_units():
                squad_hp += unit.get_health()
            if squad_hp < weakest_hp:
                weakest_squad = squad
            squad_hp = 0
        return weakest_squad