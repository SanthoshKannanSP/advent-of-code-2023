from collections import deque, defaultdict

def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")

    return data

def part1(data):
    bricks = [list(map(int, line.replace("~", ",").split(","))) for line in data]
    bricks.sort(key=lambda brick: brick[2])

    def overlaps(a, b):
        return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

    for index, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z
        
    bricks.sort(key=lambda brick: brick[2])

    k_supports_v = defaultdict(set)
    v_supports_k = defaultdict(set)

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)

    ans = 0

    for i in range(len(bricks)):
        if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
            ans += 1

    return ans

def part2(data):
    bricks = [list(map(int, line.replace("~", ",").split(","))) for line in data]
    bricks.sort(key=lambda brick: brick[2])

    def overlaps(a, b):
        return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

    for index, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z
        
    bricks.sort(key=lambda brick: brick[2])

    k_supports_v = defaultdict(set)
    v_supports_k = defaultdict(set)

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)

    ans = 0

    for i in range(len(bricks)):
        q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
        falling = set(q)
        falling.add(i)
        
        while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling:
                if v_supports_k[k] <= falling:
                    q.append(k)
                    falling.add(k)
        
        ans += len(falling) - 1

    return ans

if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))