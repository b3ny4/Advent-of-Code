
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    rules = {}
    rules_finished = False
    result = 0

    for line in lines:
        if rules_finished:
            job = [int(num) for num in line.strip().split(",")]
            valid = True
            for i, num in enumerate(job):
                if not num in rules.keys():
                    continue
                rule = rules[num]
                for follower in job[i+1:]:
                    if follower in rule:
                        valid = False

            middle = job[len(job)//2]
            if valid:
                result += middle
            print(f"{job} {valid} {middle}")
            continue
        
        if not line.strip():
            rules_finished = True
            continue
        
        a,b = [int(num) for num in line.strip().split("|")]
        if b not in rules.keys():
            rules[b] = []
        rules[b].append(a)


    print(result)
