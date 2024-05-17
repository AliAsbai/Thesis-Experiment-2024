def closest_sum(integers, queries):
    integers.sort()
    closest_sums = []

    for query in queries:
        closest_diff = float('inf')
        closest_pair = None
        left, right = 0, len(integers) - 1

        while left < right:
            current_sum = integers[left] + integers[right]
            current_diff = abs(query - current_sum)

            if current_diff < closest_diff:
                closest_diff = current_diff
                closest_pair = (integers[left], integers[right])
            
            if current_sum == query:
                break
            elif current_sum < query:
                left += 1
            else:
                right -= 1
        
        closest_sums.append((query, closest_pair))

    return closest_sums

# Main function to read input and output results
def main():
    case = 1
    while True:
        try:
            n = int(input())
            integers = [int(input()) for _ in range(n)]
            m = int(input())
            queries = [int(input()) for _ in range(m)]

            print(f"Case {case}:")
            results = closest_sum(integers, queries)
            for query, closest_pair in results:
                print(f"Closest sum to {query} is {sum(closest_pair)}.")

            case += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()
