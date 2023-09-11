import random


class Dice:
    def roll(self):
        first_random = random.randint(1, 6)
        second_random = random.randint(1, 6)
        return first_random, second_random


dice = Dice() 

result = dice.roll()
print(result)
