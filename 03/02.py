import re

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = "".join(f.readlines())

    # remove everything between any don't() and the next do() (the hacker way :P)
    donts = lines.split("don't()")
    lines = "".join(["".join(line.split("do()")[1:]) for line in donts[1:]])
    lines = donts[0]+lines

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, lines)
    result = sum([int(a)*int(b) for a,b in matches])
    print(result)
