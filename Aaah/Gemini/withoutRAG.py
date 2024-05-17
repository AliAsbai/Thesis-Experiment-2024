def compare_aah(patient_aah, doctor_aah):
  """
  Compares the length of patient's "aah" with doctor's requirement.

  Args:
      patient_aah: The "aah" the patient can say (string).
      doctor_aah: The "aah" the doctor requires (string).

  Returns:
      "go" if patient's "aah" is long enough, "no" otherwise (string).
  """

  # Remove the trailing 'h' from both strings.
  patient_aah = patient_aah[:-1]
  doctor_aah = doctor_aah[:-1]

  # Check if patient's "aah" is at least as long as doctor's requirement.
  return "go" if len(patient_aah) >= len(doctor_aah) else "no"

# Get input from the user
patient_aah = input()
doctor_aah = input()

# Call the function to compare and print the output
print(compare_aah(patient_aah, doctor_aah))
