import random

# 1. Shuffle list
def shuffle_list(original_list):
    temp_list = original_list.copy() # Parentheses are required for .copy()
    random.shuffle(temp_list)
    return temp_list

# 2. Seven unique random numbers
def seven_unique_numbers():
    # random.sample(population, k) picks k unique elements
    return random.sample(range(10), 7)