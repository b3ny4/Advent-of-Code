import re

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = "".join(f.readlines())

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, lines)
    result = sum([int(a)*int(b) for a,b in matches])
    print(result)
