def find_next_animal(prev_animal, animal_names):
    used = set()
    for animal in animal_names:
        if animal[0] == prev_animal[-1] and animal not in used:
            used.add(animal)
            if not any(name[0] == animal[-1] for name in animal_names if name != animal):
                return animal + "!"
    for animal in animal_names:
        if animal[0] == prev_animal[-1] and animal not in used:
            used.add(animal)
            return animal
    return "?"

# Sample Input Parsing
prev_animal = input().strip()
n = int(input().strip())
animal_names = [input().strip() for _ in range(n)]

# Output Calculation
output = find_next_animal(prev_animal, animal_names)
print(output)
