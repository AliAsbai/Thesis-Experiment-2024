import sys

def tape_needed(paper_sizes):
    total_sheets = 0
    total_tape = 0
    
    for i in range(len(paper_sizes)-1, -1, -1):
        total_sheets *= 2
        total_sheets += paper_sizes[i]
        
        if i == 0:
            if total_sheets != 1:
                return "impossible"
            else:
                return total_tape
        
        tape_length = (2 ** (-3/4)) / (2 ** (i / 2))
        while total_sheets >= 2:
            total_tape += tape_length * (2 ** ((i+1) / 2))
            total_sheets -= 2
            
    return "impossible"

def main():
    paper_count = int(sys.stdin.readline())
    paper_sizes = list(map(int, sys.stdin.readline().split()))
    
    result = tape_needed(paper_sizes)
    print(result)

if __name__ == "__main__":
    main()

