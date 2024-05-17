import sys
import math

def min_days_needed(n):
    if n == 1:
        return 1
    
    printers = 1
    statues_printed = 0
    days = 0
    
    while statues_printed < n:
        # If we have enough printers to print all remaining statues, print statues
        if statues_printed + printers >= n:
            days += math.ceil((n - statues_printed) / printers)
            break
        
        # Otherwise, print a new printer
        days += 1
        statues_printed += printers
        printers *= 2
        
    return days

# Read input
for line in sys.stdin:
    n = int(line)
    # Calculate and print the minimum number of days needed
    print(min_days_needed(n))
