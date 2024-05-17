def min_cabs_needed(rides):
    cabs = []
    for ride in rides:
        ride_time, source, dest = ride
        # Find a cab that can serve this ride
        found = False
        for cab in cabs:
            # Check if the cab can reach source address before departure time
            if cab[-1][0] + abs(cab[-1][1][0] - source[0]) + abs(cab[-1][1][1] - source[1]) < ride_time:
                cab.append((ride_time, dest))
                found = True
                break
        if not found:
            cabs.append([(ride_time, source), (ride_time, dest)])
    return len(cabs)

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    num_scenarios = int(lines[0])
    scenarios = []
    index = 1
    for _ in range(num_scenarios):
        num_rides = int(lines[index])
        rides = []
        for i in range(1, num_rides + 1):
            parts = lines[index + i].split()
            time = int(parts[0][:2]) * 60 + int(parts[0][3:])
            source = (int(parts[1]), int(parts[2]))
            dest = (int(parts[3]), int(parts[4]))
            rides.append((time, source, dest))
        scenarios.append(rides)
        index += num_rides + 1
    return scenarios

def main():
    input_string = '''2
2
08:00 10 11 9 16
08:07 9 16 10 11
2
08:00 10 11 9 16
08:06 9 16 10 11'''

    scenarios = parse_input(input_string)
    for rides in scenarios:
        print(min_cabs_needed(rides))

if __name__ == "__main__":
    main()
