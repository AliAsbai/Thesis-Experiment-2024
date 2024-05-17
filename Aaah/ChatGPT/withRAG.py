import sys

for line in sys.stdin:
    jon_marius_input = line.strip()
    doctor_input = next(sys.stdin).strip()
    
    if len(jon_marius_input) >= len(doctor_input):
        print("go")
    else:
        print("no")
