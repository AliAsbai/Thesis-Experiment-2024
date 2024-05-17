#! /usr/bin/python3

animals = {}

# Read input
last_animal = input().strip()
num_animals = int(input())

for _ in range(num_animals):
  animal = input().strip()
  first_letter = animal[0]
  animals.setdefault(first_letter, []).append(animal)

# Check for winning move
last_letter = last_animal[-1]
if last_letter in animals:
  for candidate in animals[last_letter]:
    # Check if next player can't play anything (no key for last letter)
    if candidate[-1] not in animals:
      print(candidate + "!")
      exit(0)
  # No elimination move, but can still play a valid move
  print(animals[last_letter][0])
else:
  # No valid move based on last letter, bluff
  print("?")
