if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    rules = {}
    rules_finished = False
    result = 0
    incorrect = []

    def isSmaller(p1, p2):
        if not p1 in rules.keys():
            return True
        if not p2 in rules[p1]:
            return True
        return False

    def bubblesort(job):
        result = [1]
        while len(job) > 0:
            for p1 in job:
                smallest = True
                for p2 in job:
                    if not isSmaller(p1, p2):
                        smallest = False
                        break
                if smallest:
                    job.remove(p1)
                    result.append(p1)
                    
        return result

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

            if not valid:
                job = bubblesort(job)
                middle = job[len(job)//2]
                #print(f"{job} {valid} {middle}")
                result += middle
            continue
        
        if not line.strip():
            rules_finished = True
            continue
        
        a,b = [int(num) for num in line.strip().split("|")]
        if b not in rules.keys():
            rules[b] = []
        rules[b].append(a)


    print(result)
