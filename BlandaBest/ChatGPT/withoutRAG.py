def main():
    n = int(input().strip())
    meats = set()

    for _ in range(n):
        meat_type = input().strip()
        meats.add(meat_type)

    if "nautakjot" in meats and "kjuklingur" in meats:
        print("blandad best")
    elif "nautakjot" in meats:
        print("nautakjot")
    elif "kjuklingur" in meats:
        print("kjuklingur")

if __name__ == "__main__":
    main()
