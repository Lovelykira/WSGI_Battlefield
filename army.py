from random_strategy import RandomStrategy


class Army:
    def __init__(self, strategy=RandomStrategy):
        self._squads = []
        self._strategy = strategy

    def get_alive_squads(self):
        alive_squads = []
        for squad in self._squads:
            if squad.is_alive():
                alive_squads.append(squad)
        return alive_squads

    def take_damage(self, squad, dmg):
        squad.take_damage(dmg)

    def attack(self, enemy):
        while True:
            for squad in self._squads:
                if not squad.is_alive() or squad.recharge():
                    continue

                print("\n\tAttacker's army has {} squads left".format(len(self.get_alive_squads())))
                print("\tDefender's army has {} squads left\n".format(len(enemy.get_alive_squads())))
                enemy_squad = self._strategy.chose_squad(enemy_army=enemy)
                print("Attacker's {}".format(str(squad)))
                print("Defender's {}".format(str(enemy_squad)))

                dmg = squad.attack()
                print("\nAttacker's dmg = {}".format(dmg))
                enemy.take_damage(enemy_squad, dmg)
                if enemy_squad.is_alive() and not enemy_squad.recharge():
                    return_dmg = enemy_squad.attack()
                    print("Defender's dmg = {}".format(return_dmg))
                    self.take_damage(squad, return_dmg)
                    if not squad.is_alive():
                        print("\n\tATTACKER'S SQUAD DIES!\n")
                elif not enemy_squad.is_alive():
                    print("\n\tDEFENDER'S SQUAD DIES!\n")
                else:
                    print("\nDefender is charging")


            if len(self.get_alive_squads()) == 0:
                print("Defender wins\n")
                break
            if len(enemy.get_alive_squads()) == 0:
                print("Attacker wins\n")
                break

    def add_group(self, group):
        self._squads.append(group)

    def is_alive(self):
        if len(self.get_alive_squads()) != 0:
            return True
        else:
            return False

    def get_strategy(self):
        return self._strategy.__name__
