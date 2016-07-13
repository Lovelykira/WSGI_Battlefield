from random_strategy import RandomStrategy


class Army:
    def __init__(self, strategy=RandomStrategy):
        self._squads = []
        self._strategy = strategy

    def get_alive_squads(self):
        alive_squads = []
        for squad in self._squads:
            if squad.is_alive():
                #print("SQUAD IS ALIVE",squad)
                alive_squads.append(squad)
        return alive_squads

    def take_damage(self, squad, dmg):
        #print("squad: ",squad)
        squad.take_damage(dmg)

    def attack(self, enemy):
        res = ""
        i=0
        while True:
            for squad in self._squads:

                if not squad.is_alive() or squad.recharge():
                    continue
                res += "<br>&ensp;Attacker's army has {} squad(s) left".format(len(self.get_alive_squads()))
                res += "<br>&ensp;Defender's army has {} squad(s) left<br>".format(len(enemy.get_alive_squads()))
                enemy_squad = self._strategy.chose_squad(enemy_army=enemy)

                res += "<br>Attacker's {}".format(str(squad))
                res += "<br>Defender's {}".format(str(enemy_squad))

                dmg = squad.attack()
                res +="<br>Attacker's dmg = {}".format(dmg)
                enemy.take_damage(enemy_squad, dmg)
                if enemy_squad.is_alive() and not enemy_squad.recharge():
                    return_dmg = enemy_squad.attack()
                    res += "<br>Defender's dmg = {}<br>".format(return_dmg)
                    self.take_damage(squad, return_dmg)
                    if not squad.is_alive():
                        res += "<br>&ensp;ATTACKER'S SQUAD DIES!"
                elif not enemy_squad.is_alive():
                    res += "<br>&ensp;DEFENDER'S SQUAD DIES!\n"
                else:
                    res += "<br>Defender is charging"

            if len(self.get_alive_squads()) == 0:
                res += "<br>&ensp;Defender wins\n"
                break
            if len(enemy.get_alive_squads()) == 0:
                res += "<br>&ensp;Attacker wins\n"
                break

        return res

    def add_group(self, group):
        self._squads.append(group)

    def is_alive(self):
        if len(self.get_alive_squads()) > 0:
            return True
        else:
            return False

    def get_strategy(self):
        return self._strategy.__name__

    def __str__(self):
        squads = self.get_alive_squads()
        squads = '\n'.join([str(squad) for squad in squads])
        return 'Army with {} units: \n{}'.format(len(self.get_alive_squads()), squads)
