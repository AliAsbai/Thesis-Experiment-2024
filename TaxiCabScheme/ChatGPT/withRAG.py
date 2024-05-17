import sys

def min_cabs_required(rides):
    cabs = []
    for ride in rides:
        found_cab = False
        for cab in cabs:
            if cab[-1][0] <= ride[0]:
                cab.append(ride)
                found_cab = True
                break
        if not found_cab:
            cabs.append([ride])
    return len(cabs)

def main():
    for line in sys.stdin:
        num_test_cases = int(line.strip())
        for _ in range(num_test_cases):
            num_rides = int(input().strip())
            rides = []
            for _ in range(num_rides):
                departure_time, a, b, c, d = input().strip().split()
                departure_hour, departure_minute = map(int, departure_time.split(':'))
                ride = (departure_hour * 60 + departure_minute, int(a), int(b), int(c), int(d))
                rides.append(ride)
            result = min_cabs_required(rides)
            print(result)

if __name__ == "__main__":
    main()
