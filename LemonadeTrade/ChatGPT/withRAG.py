import sys

def max_blue_lemonade(trades):
    pink_lemonade = 1.0  # Start with 1 liter of pink lemonade
    blue_lemonade = 0.0
    for offer, want, rate in trades:
        if want == "pink":
            if offer == "blue":
                blue_lemonade += pink_lemonade / rate
                pink_lemonade = 0.0
            else:
                pink_lemonade -= pink_lemonade / rate
        elif want == "blue":
            if offer == "blue":
                blue_lemonade += rate
            else:
                blue_lemonade += pink_lemonade * rate
                pink_lemonade = 0.0
    return min(blue_lemonade, 10.0)

if __name__ == "__main__":
    trades = []
    for line in sys.stdin:
        data = line.strip().split()
        if len(data) == 1:
            n = int(data[0])
            break
        trades.append((data[0], data[1], float(data[2])))

    result = max_blue_lemonade(trades)
    print("{:.16f}".format(result))
