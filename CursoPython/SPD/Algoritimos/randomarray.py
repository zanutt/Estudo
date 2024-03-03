#apenas um gerador de array para testes

import random

def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

array_size = 20
min_value = 0
max_value = 50

random_array = generate_random_array(array_size, min_value, max_value)
print("Array aleatório gerado:", random_array)