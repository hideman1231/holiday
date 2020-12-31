from random import randint
from exception import GameOver, EnemyDown

class GameEntity:
    def __init__(self,hearts,damage,armor,critical):
        self.hearts = hearts
        self.damage = damage
        self.armor = armor
        self.critical = critical

    @staticmethod
    def miss():
        return randint(1,8)

    @staticmethod
    def creet():
        return randint(1,5)

    def defense(self,hit,crit):
        if self.miss() == 1:
            print("miss")
        if self.creet() == 1:
            if self.hearts - hit * crit / self.armor < 0:
                self.hearts = 0
                raise GameOver("You lose")
            else:
                self.hearts -= hit * crit / self.armor 
                print("creet")
                print("my hp:" , round(self.hearts, 2))
        else:
            if self.hearts - hit / self.armor < 0:
                self.hearts = 0
                raise GameOver("You lose")
            else:
                self.hearts -= hit / self.armor
                print("my hp:" , round(self.hearts, 2))


class Dragon(GameEntity):
    def __init__(self,hearts,damage,armor,critical):
        super().__init__(hearts,damage,armor,critical)






a = GameEntity(20,2,5,2)
b = Dragon(20,2,5,10)

a.defense(b.damage,b.critical)
a.defense(b.damage,b.critical)
a.defense(b.damage,b.critical)
