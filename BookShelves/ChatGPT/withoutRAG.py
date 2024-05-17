def min_shelves_needed(books, shelf_width):
    total_width = sum((count * width) for width, count in enumerate(books, start=1))
    shelves_needed = total_width // shelf_width
    if total_width % shelf_width != 0:
        shelves_needed += 1
    return shelves_needed

if __name__ == "__main__":
    books = list(map(int, input().split()))
    shelf_width = int(input())
    print(min_shelves_needed(books, shelf_width))
