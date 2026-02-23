import random
import string

# 1. Generate a six-digit/character random_user_id
def random_user_id():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

# 2. User-defined ID generation
def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs: "))
    
    chars = string.ascii_letters + string.digits
    for _ in range(num_ids):
        user_id = ''.join(random.choice(chars) for _ in range(num_chars))
        print(user_id)

# 3. RGB Color Generator
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"