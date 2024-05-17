import sys

def swap_ants(ants, idx):
    ants[idx], ants[idx - 1] = ants[idx - 1], ants[idx]

def main():
    for line in sys.stdin:
        N1, N2 = map(int, line.split())
        ants1 = list(input().strip())
        ants2 = list(input().strip())
        T = int(input().strip())

        for _ in range(T):
            idx_to_move = []
            for i in range(len(ants1) - 1, -1, -1):
                if i >= N1 and i < len(ants1) - 1 and ants1[i] in ants2 and ants1[i - 1] in ants2:
                    idx_to_move.append(i)

            for idx in idx_to_move:
                swap_ants(ants1, idx)

            idx_to_move = []
            for i in range(1, len(ants2)):
                if i < N1 and ants2[i] in ants1 and ants2[i - 1] in ants1:
                    idx_to_move.append(i)

            for idx in idx_to_move:
                swap_ants(ants2, idx)

        ants1.extend(ants2)
        if ants1[0] in ants2:
            print(''.join(ants1[::-1]))
        else:
            print(''.join(ants1))

if __name__ == "__main__":
    main()
