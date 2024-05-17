import sys

def process_applications(C, A, incomes):
    cost_of_living = {}  # Dictionary to store the cost of living for each city

    for i in range(A):
        # Keep track of the remaining budget
        budget = 1500 - len(cost_of_living)

        # If we have enough budget to ask for the cost of living of a city
        if budget > 0:
            print("Q", min(len(cost_of_living) + 1, C))
            sys.stdout.flush()
            cost = int(input().strip())
            cost_of_living[len(cost_of_living) + 1] = cost

        # Determine the city to suggest for the pony
        for city, cost in sorted(cost_of_living.items(), key=lambda x: x[1], reverse=True):
            if incomes[i] >= cost:
                print("A", city)
                sys.stdout.flush()
                break

# Read input
C, A = map(int, input().split())
incomes = list(map(int, input().split()))

# Process applications
process_applications(C, A, incomes)
