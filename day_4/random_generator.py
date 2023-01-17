import random

random_int = random.randint(1, 1000)
random_float = random.random() * 5
real_random_float = "{:.3f}".format(random_float)
print(real_random_float)
print(random_int)