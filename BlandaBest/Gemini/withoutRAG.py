def get_niels_meat(meat_types):
  """
  This function determines the type of meat Níels got on his kebab.

  Args:
      meat_types: A list of strings representing the meat types offered
                  (either "nautakjot" or "kjuklingur").

  Returns:
      A string representing the type of meat Níels got:
          - "nautakjot" if only beef offered
          - "kjuklingur" if only chicken offered
          - "blandad best" (mixed) if both beef and chicken offered
  """
  # Check if both options are available (mixed)
  if "nautakjot" in meat_types and "kjuklingur" in meat_types:
    return "blandad best"
  # Otherwise, return the single offered meat type
  else:
    return meat_types[0]

# Get number of meat types
num_types = int(input())

# Read the meat types
meat_types = []
for _ in range(num_types):
  meat_types.append(input().strip())

# Get Níels' meat
niels_meat = get_niels_meat(meat_types)

# Print the output
print(niels_meat)
