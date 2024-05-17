import sys

def battle_winner(ng, nm, godzilla_army, mechagodzilla_army):
    godzilla_army.sort()
    mechagodzilla_army.sort()

    if godzilla_army[0] < mechagodzilla_army[0]:
        return "Godzilla"
    elif godzilla_army[0] > mechagodzilla_army[0]:
        return "MechaGodzilla"
    else:
        return "uncertain"

def main():
    T = int(input().strip())
    input()  # Consume blank line

    for _ in range(T):
        NG, NM = map(int, input().strip().split())
        godzilla_army = list(map(int, input().strip().split()))
        mechagodzilla_army = list(map(int, input().strip().split()))

        winner = battle_winner(NG, NM, godzilla_army, mechagodzilla_army)
        print(winner)

if __name__ == "__main__":
    main()
