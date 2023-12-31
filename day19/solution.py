def load():
    with open("input.txt","r") as f:
        data = f.read().strip()
        
    return data

def part1(data):
    block1, block2 = data.split("\n\n")
    workflows = {}

    for line in block1.split("\n"):
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    ops = {">": int.__gt__, "<": int.__lt__}


    def accept(item, name="in"):
        if name == "R":
            return False
        if name == "A":
            return True

        rules, fallback = workflows[name]

        for key, cmp, n, target in rules:
            if ops[cmp](item[key], n):
                return accept(item, target)

        return accept(item, fallback)


    ans = 0

    for line in block2.split("\n"):
        item = {}
        for segment in line[1:-1].split(","):
            ch, n = segment.split("=")
            item[ch] = int(n)
        if accept(item):
            ans += sum(item.values())

    return ans

def part2(data):
    block1, _ = data.split("\n\n")
    workflows = {}

    for line in block1.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    def count(ranges, name = "in"):
        if name == "R":
            return 0
        if name == "A":
            product = 1
            for lo, hi in ranges.values():
                product *= hi - lo + 1
            return product
        
        rules, fallback = workflows[name]

        ans = 0

        for key, cmp, n, target in rules:
            lo, hi = ranges[key]
            if cmp == "<":
                T = (lo, min(n - 1, hi))
                F = (max(n, lo), hi)
            else:
                T = (max(n + 1, lo), hi)
                F = (lo, min(n, hi))
            if T[0] <= T[1]:
                copy = dict(ranges)
                copy[key] = T
                ans += count(copy, target)
            if F[0] <= F[1]:
                ranges = dict(ranges)
                ranges[key] = F
            else:
                break
        else:
            ans += count(ranges, fallback)
                
        return ans

    return count({key: (1, 4000) for key in "xmas"})

if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))