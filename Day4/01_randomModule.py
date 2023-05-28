import random

# The mersenne twister algorithm is used to generate sudo random numbers.
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

print(random_integer + random_float)
