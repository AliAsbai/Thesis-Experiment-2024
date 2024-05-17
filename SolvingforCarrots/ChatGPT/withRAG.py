import sys

def main():
    for line in sys.stdin:
        data = line.split()
        if len(data) == 2:
            N, P = map(int, data)
            break

    print(P)

if __name__ == "__main__":
    main()
