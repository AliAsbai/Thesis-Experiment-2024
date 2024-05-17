import sys

def battle_outcome(ng_strengths, nm_strengths):
    ng_strengths.sort()
    nm_strengths.sort()
    while ng_strengths and nm_strengths:
        if ng_strengths[0] < nm_strengths[0]:
            ng_strengths.pop(0)
        elif ng_strengths[0] > nm_strengths[0]:
            nm_strengths.pop(0)
        else:
            nm_strengths.pop(0)
    if ng_strengths:
        return "Godzilla"
    elif nm_strengths:
        return "MechaGodzilla"
    else:
        return "uncertain"

for line in sys.stdin:
    t = int(line.strip())
    for _ in range(t):
        input()  # Blank line
        ng, nm = map(int, input().split())
        ng_strengths = list(map(int, input().split()))
        nm_strengths = list(map(int, input().split()))
        result = battle_outcome(ng_strengths, nm_strengths)
        print(result)
