import sys

for line in sys.stdin:
    a = int(line)
    ratio_option_one = 100 / a
    ratio_option_two = 100 / (100 - a)
    print("{:.10f}".format(ratio_option_one))
    print("{:.10f}".format(ratio_option_two))
