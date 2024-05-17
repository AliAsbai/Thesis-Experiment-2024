def simulate_die(dice1, dice2, dice3, target_die):
  """
  Checks if the target die can be simulated using the probabilities of the given dice.

  Args:
      dice1: A tuple representing probabilities (outcome1, outcome2, outcome3) for die 1.
      dice2: A tuple representing probabilities (outcome1, outcome2, outcome3) for die 2.
      dice3: A tuple representing probabilities (outcome1, outcome2, outcome3) for die 3.
      target_die: A tuple representing probabilities (outcome1, outcome2, outcome3) for the target die.

  Returns:
      True if the target die can be simulated, False otherwise.
  """
  total_prob = sum(dice1) + sum(dice2) + sum(dice3)
  if total_prob != 10000:  # Probabilities don't sum to 1
    return False

  # Solve a system of equations to find weights for each die
  # x * dice1 + y * dice2 + z * dice3 = target_die
  # x + y + z = 1 (weights sum to 1)
  # We can represent this as a matrix equation Ax = b
  A = [[dice1[0], dice2[0], dice3[0], 1],
       [dice1[1], dice2[1], dice3[1], 1],
       [dice1[2], dice2[2], dice3[2], 1]]
  b = list(target_die)

  # Check for degenerate cases (all-zero rows/columns or proportional rows)
  if all(x == 0 for x in A[0]):  # All elements in first row are zero
    if b[0] == 0 and all(a == b for a, b in zip(b[1:], dice2[1:])):
      return True  # Solution exists (weights are 1 for proportional dice2 and die3)
    else:
      return False  # No solution for this case
  elif any(all(row[i] == 0 for row in A[1:]) for i in range(len(A[0]))):
    # Any column (except the first element) has all zeros
    return False  # No solution for this case with a zero column
  elif any(a == b for a, b in zip(A[0], A[1])) or any(a == b for a, b in zip(A[0], A[2])):
    # Proportional rows (weights cannot be unique)
    return False  # No solution for this case with proportional rows

  # Calculate determinant using a modified version of calculate_determinant
  determinant = calculate_determinant(A)

  # Check if determinant is zero (non-singular matrix)
  if determinant == 0:
    return False

  # Solve for weights using Cramer's rule
  weights = []
  for i in range(4):
    new_b = b.copy()
    for j in range(4):
      if i != j:
        new_b[j] = A[j][i]
    weights.append(calculate_determinant([*new_b[:i], *new_b[i+1:]]) / determinant)

  # Check if weights are non-negative and within range (0 to 1)
  for weight in weights:
    if weight < 0 or weight > 1:
      return False

  return True

def calculate_determinant(matrix):
  """
  Calculates the determinant of a 3x3 matrix using recursion with special case handling.
  """
  if len(matrix) == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  else:
    determinant = 0
    for i in range(len(matrix[0])):
      # Check if the current column has all zeros (except the first element)
      if all(row[i] == 0 for row in matrix[1:]):
        continue  # Skip if the column is all zeros (except the first element)
      minor = [[row[j] for j in range(len(row)) if j != i] for row in matrix[1:]]
      determinant += matrix[0]
