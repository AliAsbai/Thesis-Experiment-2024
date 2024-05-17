def min_days_to_print_statues(n):
    printers = 1  # Initial number of printers
    statues_printed = 0
    days = 0
    
    while statues_printed < n:
        # On each day, we either print statues or print more printers
        days += 1
        statues_printed += printers  # Print statues with available printers
        if statues_printed >= n:
            break
        printers += 1  # Increase the number of printers by 1
        
    return days

# Sample Input
n = int(input("Enter the number of statues: "))

# Output
print("Minimum number of days needed:", min_days_to_print_statues(n))
