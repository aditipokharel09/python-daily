def add_all_nums(*args):
    total = 0
    for n in args:
        if not isinstance(n, (int, float)):
            return "Error: All items must be numbers!"
        total += n
    return total