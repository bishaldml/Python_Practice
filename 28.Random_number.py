import random

# 1.
x = random.randint(1,10)
print(x)

# 2.
cards = [1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']

z = random.choice(cards)
print(z)

# 3.
random.shuffle(cards)
print(cards)