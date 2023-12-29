import re


def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


# (t-x)x > d
# tx - xx > d
# xx-tx+d<0


def solve(t, s):
    s += 1e-6
    d = (t**2) - (4 * s)
    root1 = (t - d**0.5) // 2
    root2 = (t + d**0.5) // 2

    return root1, root2


def part1(data):
    times = list(map(int, re.findall(r"\d+", data[0])))
    distances = list(map(int, re.findall(r"\d+", data[1])))

    n = len(times)
    ans = 1
    for i in range(n):
        low, high = solve(times[i], distances[i])
        ans *= high - low

    return int(ans)


def part2(data):
    time = int("".join(re.findall(r"\d+", data[0])))
    distance = int("".join(re.findall(r"\d+", data[1])))

    low, high = solve(time, distance)

    return int(high - low)


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
