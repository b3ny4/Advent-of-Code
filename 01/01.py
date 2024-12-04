
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [[int(x) for x in line.strip().split("   ")] for line in f.readlines()]

    l, r = zip(*lines)

    l = sorted(l)
    r = sorted(r)

    print(sum([abs(l-r) for l, r in zip(l, r)]))
