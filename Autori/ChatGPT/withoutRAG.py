def long_to_short(name):
    parts = name.split('-')
    short_name = ''
    for part in parts:
        short_name += part[0]
    return short_name

# Reading input
long_variation = input()

# Transforming and printing output
short_variation = long_to_short(long_variation)
print(short_variation)
