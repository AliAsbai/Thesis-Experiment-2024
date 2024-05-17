#! /usr/bin/python3

def compare_aah(jon_marius_aah, doctor_aah):
  """Compares the length of Jon Marius's aah with the doctor's requirement.

  Args:
      jon_marius_aah: The string representing Jon Marius's aah.
      doctor_aah: The string representing the doctor's requirement.

  Returns:
      "go" if Jon Marius's aah is long enough, "no" otherwise.
  """

  # Remove trailing characters (including 'h') from both strings.
  jon_marius_aah = jon_marius_aah.rstrip('ah')
  doctor_aah = doctor_aah.rstrip('ah')

  # Compare the lengths of the remaining strings.
  if len(jon_marius_aah) >= len(doctor_aah):
    return "go"
  else:
    return "no"

for line in sys.stdin:
  # Read both lines of input.
  jon_marius_aah = line.strip()
  doctor_aah = sys.stdin.readline().strip()

  # Call the function to compare the aahs and print the result.
  print(compare_aah(jon_marius_aah, doctor_aah))
