# TODO: POC! needs cleanup!

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]

    safelines = [False for _ in range(len(lines))]

    for idx, line in enumerate(lines):
        increasing = True
        last = 0
        safe = True
        dampener = True
        for i,n in enumerate(line):
            if i == 0:
                last = n
                continue
            if i == 1:
                increasing = n>last

            if abs(last-n) > 3:
                if dampener:
                    dampener = False
                    continue
                safe = False
                break

            if increasing and n<=last:
                if dampener:
                    dampener = False
                    continue
                safe = False
                break

            if not increasing and n>=last:
                if dampener:
                    dampener = False
                    continue
                safe = False
                break

            last = n

        if safe:
            safelines[idx] = True
            #print(f"{line}: {safe}")
            continue

        increasing = True
        last = 0
        safe = True
        for i,n in enumerate(line):
            if i == 0:
                last = n
                continue
            if i == 1:
                continue
            if i == 2:
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
            safelines[idx] = True
            print(f"{line}: {safe}")
            continue

        increasing = True
        last = 0
        safe = True
        for i,n in enumerate(line):
            if i == 1:
                last = n
                continue
            if i == 0:
                continue
            if i == 2:
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
            safelines[idx] = True
            print(f"{line}: {safe}")
            continue

    print(safelines.count(True))