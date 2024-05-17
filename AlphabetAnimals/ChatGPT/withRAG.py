import sys

def main():
    # Read input
    previous_animal = input().strip()
    n = int(input().strip())
    animal_names = [input().strip() for _ in range(n)]
    
    # Create a dictionary to store animal names by their first letter
    animal_dict = {}
    for name in animal_names:
        first_letter = name[0]
        if first_letter in animal_dict:
            animal_dict[first_letter].append(name)
        else:
            animal_dict[first_letter] = [name]
    
    # Check if there are any valid options
    if previous_animal[-1] in animal_dict:
        valid_options = animal_dict[previous_animal[-1]]
        for name in valid_options:
            if name[-1] not in animal_dict or (len(animal_dict[name[-1]]) == 1 and animal_dict[name[-1]][0] == name):
                print(name + "!")
                return
        print(valid_options[0])
    else:
        print("?")

if __name__ == "__main__":
    main()
