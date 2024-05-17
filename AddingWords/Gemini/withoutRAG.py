definitions = {}  # Dictionary to store word-number mappings

def handle_definition(word, value):
  """Defines a word with a corresponding numerical value."""
  if not word.islower() or not word.isalpha():
    print("Invalid word:", word)
    return
  definitions[word] = value

def handle_calculation(expression):
  """Calculates the sum/difference of defined words and prints the result."""
  result = 0
  unknown = False
  for term in expression.split():
    if term in "+-=":
      continue
    term = term.lower()  # Convert term to lowercase for case-insensitive handling
    if term not in definitions:
      unknown = True
      break
    try:
      result += definitions[term] * (-1 if term in "-=" else 1)
    except KeyError:
      unknown = True  # Handle missing definition during calculation
      break
  if unknown:
    print(expression, "= unknown")
  else:
    word_result = get_word_for_number(result)
    if word_result:
      print(expression, "=", word_result)
    else:
      print(expression, "= unknown")

def handle_clear():
  """Clears all definitions."""
  global definitions
  definitions = {}

def get_word_for_number(number):
  """Returns the defined word for a number (if exists), otherwise None."""
  for word, value in definitions.items():
    if value == number:
      return word
  return None

def main():
  """Reads input commands and processes them."""
  for line in iter(input, ""):
    command = line.strip().split()
    if len(command) < 2:
      print("Invalid command:", line.strip())
      continue
    if command[0] == "def":
      try:
        handle_definition(command[1], int(command[2]))
      except ValueError:
        print("Invalid definition:", line.strip())
    elif command[0] == "calc":
      handle_calculation(" ".join(command[1:]))
    elif command[0] == "clear":
      handle_clear()
    else:
      print("Invalid command:", line.strip())

if __name__ == "__main__":
  main()
