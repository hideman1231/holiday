from models import Warrior, Dragon
from exception import GameOver, EnemyDown

def game():
	hero = input("Выберите героя: ")
	if hero == Warrior:
		player = Warrior(10,5,4)
	elif hero == Wizard:
		player = Wizard(7,12,6)
	elif hero == Archer:
		player == Archer(8,9,5)
	enemy = Dragon(40,3,2)
	while True:
		player.defense(enemy.damage)
		enemy.defense(player.damage)

if __name__ == '__main__':
	try:
		game()
	except EnemyDown:
		print("You win")
	except GameOver:
		print("You lose!")