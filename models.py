from random import randint
from exception import GameOver, EnemyDown

class Warrior:
    def __init__(self,hearts,damage,armor):
        self.hearts = hearts
        self.damage = damage
        self.armor = armor

    @staticmethod
    def warrior_miss():
        return randint(1,8)

    def defense(self,hit):
        if self.warrior_miss() == 1:
            print("miss")
        else:
            if self.hearts - hit / self.armor < 0:
                self.hearts = 0
                raise GameOver("You lose")
            else:
                self.hearts -= hit / self.armor
                print("my hp:" , round(self.hearts, 2))


class Dragon:
    def __init__(self,hearts,damage,armor):
        self.hearts = hearts
        self.damage = damage 
        self.armor = armor

    def defense(self,hit):
        if self.hearts - hit / self.armor < 0:
            self.hearts = 0
            raise EnemyDown
        else:
            self.hearts -= hit / self.armor
            print("drago hp:" , round(self.hearts, 2))





