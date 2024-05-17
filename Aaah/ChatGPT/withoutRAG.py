def can_go_to_doctor(jon_marius_aah, doctor_aah):
    return "go" if len(jon_marius_aah) >= len(doctor_aah) else "no"

# Read input
jon_marius_aah = input().strip()
doctor_aah = input().strip()

# Check if Jon Marius can go to the doctor
result = can_go_to_doctor(jon_marius_aah, doctor_aah)
print(result)
