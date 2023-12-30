def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def solve(nums):
    if all(n == 0 for n in nums):
        return 0

    diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

    return nums[-1] + solve(diff)


def part1(data):
    ans = 0
    for line in data:
        values = list(map(int, line.split()))
        ans += solve(values)

    return ans


def part2(data):
    ans = 0
    for line in data:
        values = list(map(int, line.split()))
        ans += solve(values[::-1])

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
