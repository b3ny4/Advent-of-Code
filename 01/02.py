

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [[int(x) for x in line.strip().split("   ")] for line in f.readlines()]

    lefts, rights = zip(*lines)

    similarity = 0

    for left in lefts:
        num = rights.count(left)
        similarity += left*num

    print(similarity)
