from random import *
import time
from abc import *


class Unit(metaclass=ABCMeta):
    health = 100
    recharge = randint(100,2000)
    next_attack_time = 0
    armor = 0

    @abstractmethod
    def do_attack(self):
        self.next_attack_time = time.time() + self.recharge
        return 0

    @abstractmethod
    def take_damage(self, dmg):
        self.health -= dmg + self.armor

    def can_attack(self):
        if time.time() >= self.next_attack_time and self.is_alive():
            return True
        else:
            return False

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Soilder(Unit):
    experience = 0

    def do_attack(self):
        if self.can_attack():
            self.next_attack_time = time.time() + self.recharge
            if self.experience != 50:
                self.experience += 1
            print("sol dmg=", 0.5 * (1 + self.health / 100) * randint(50 + self.experience, 100) / 100)
            return 0.5 * (1 + self.health / 100) * randint(50 + self.experience, 100) / 100
        else:
            return 0

    def take_damage(self, dmg):
        self.armor = self.calc_armor()
        self.health -= dmg + self.armor

        print("DMG:", dmg, "ARM:",self.armor)

    def calc_armor(self):
        return 0.05 + self.experience / 100


class Vehicle(Unit):
    def __init__(self):
        self.operators = []
        num_oper = randint(1,3)
        for i in range(num_oper):
            self.operators.append(Soilder())
        print("len oper",len(self.operators))

    def do_attack(self):
        if self.can_attack():
            self.next_attack_time = time.time() + self.recharge
            op_sum_attack = 0
            for op in self.operators:
                op_sum_attack += op.do_attack()
            print("veh dmg = ", self.operators )
            return 0.5 * (1 + self.health / 100) * op_sum_attack / len(self.operators)
        else:
            return 0

    def take_damage(self, dmg):
        veh_dmg = dmg * 0.6
        self.armor = self.calc_armor()
        self.health -= veh_dmg + self.armor
        print("DMG:", veh_dmg, "ARM:",self.armor)
        rnd_op_dmg = dmg * 0.2
        rnd_op = randint(0, len(self.operators)-1)
        self.operators[rnd_op].take_damage(rnd_op_dmg)
        for i in range(len(self.operators)):
            if i != rnd_op:
                self.operators[i].take_damage(dmg * 0.1)

    def calc_armor(self):
        op_sum_exp = 0
        for op in self.operators:
            op_sum_exp += op.experience / 100
        return 0.1 + op_sum_exp


class Squad:
    def __init__(self):
        self.units = []
        num_units = randint(1,3)
        for i in range(num_units):
            self.units.append(Soilder())
        print("squad num un=", len(self.units))

        num_veh = randint(1,3)
        for i in range(num_veh):
            self.units.append(Vehicle())

    def attack(self):
        power = 0
        for unit in self.units:
            power += unit.do_attack()
        print("squad dmg=", power)
        return power / len(self.units)

    def take_damage(self, dmg):
        dmg_per_unit = dmg / len(self.units)
        for unit in reversed(self.units):
            unit.take_damage(dmg_per_unit)
            if not unit.is_alive:
                self.units.remove(unit)

    def is_alive(self):
        for unit in self.units:
            if unit.is_alive():
                return True
        return False


class Army:
    squads = []

    def __init__(self):
        num_squads = randint(1,3)
        for i in range(num_squads):
            self.squads.append(Squad())

    def get_squads(self):
        return self.squads

    def take_damage(self, squad, dmg):
        #self.squads[squad_num].take_damage(dmg)
        squad.take_damage(dmg)

    def squad_died(self, squad):
        if squad.is_alive():
            return False
        self.squads.remove(squad)
        return True


    def attack(self, enemy):

        while True:
            for squad in reversed(self.squads):
                num_squad = randint(0, len(enemy.get_squads())-1)
                print("units:",len(squad.units))
                print("units:", len(enemy.get_squads()[num_squad].units))
                for unit in squad.units:
                    print("our unit's hp: ", unit.health)
                for unit in enemy.get_squads()[num_squad].units:
                    print("enemy unit's hp: ", unit.health)

                dmg = squad.attack()
                print("try_dmg=", dmg)
                enemy.take_damage(enemy.get_squads()[num_squad], dmg)
                if not enemy.squad_died(enemy.get_squads()[num_squad]):
                    return_dmg = enemy.get_squads()[num_squad].attack()
                    self.take_damage(squad,return_dmg)
                    self.squad_died(squad)
            if self.get_squads() == []:
                print("We lose")
                break
            if enemy.get_squads() == []:
                print("We win")
                break



class  Battlefield:
    armies = [Army(), Army()]
    def start(self):
        self.armies[0].attack(self.armies[1])


b = Battlefield()

b.start()



