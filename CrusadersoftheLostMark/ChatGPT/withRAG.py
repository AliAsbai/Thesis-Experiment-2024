import sys

def main():
    # Read input
    C, A = map(int, input().split())
    incomes = list(map(int, input().split()))
    
    # Initialize variables
    remaining_budget = 1500
    queried_cities = set()

    # Process each application
    for income in incomes:
        max_cost = None
        suggested_city = None
        
        # Perform binary search only if the city's cost hasn't been queried before
        if len(queried_cities) < C:
            for i in range(C):
                if i + 1 not in queried_cities:
                    print("Q", i + 1)
                    sys.stdout.flush()
                    cost = int(input())
                    queried_cities.add(i + 1)
                    remaining_budget -= 1
                    if remaining_budget == 0:
                        break

        # Find the maximum affordable city
        for city in sorted(queried_cities):
            if city <= income:
                suggested_city = city
            else:
                break

        # Output suggestion
        print("A", suggested_city)
        sys.stdout.flush()

    sys.stdout.flush()

if __name__ == "__main__":
    main()
