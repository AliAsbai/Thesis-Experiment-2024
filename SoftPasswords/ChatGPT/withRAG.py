import sys

def is_accepted(S, P):
    if S == P:
        return True
    
    if len(S) == len(P):
        for i in range(len(S)):
            if S[i].isdigit():
                if not P[i].isdigit() or S[i] != P[i]:
                    return False
            elif S[i].islower():
                if P[i].lower() != S[i]:
                    return False
            elif S[i].isupper():
                if P[i].upper() != S[i]:
                    return False
        return True
    
    if len(P) > len(S):
        return False
    
    if S[-1].isdigit() and S[:-1] == P:
        return True
    
    if S[0].isdigit() and S[1:] == P:
        return True
    
    return False

if __name__ == "__main__":
    S = input().strip()
    P = input().strip()
    
    if is_accepted(S, P):
        print("Yes")
    else:
        print("No")
