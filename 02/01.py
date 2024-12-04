
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]

    num_safe = 0

    for line in lines:
        increasing = True
        last = 0
        safe = True
        for i,n in enumerate(line):
            if i == 0:
                last = n
                continue
            if i == 1:
                increasing = n>last

            if abs(last-n) > 3:
                safe = False
                break

            if increasing and n<=last:
                safe = False
                break

            if not increasing and n>=last:
                safe = False
                break

            last = n

        if safe:
            num_safe+=1

    print(num_safe)