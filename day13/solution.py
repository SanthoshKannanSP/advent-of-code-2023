def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n\n")

    return data


def find_mirror(grid):
    for i in range(1, len(grid)):
        above = grid[:i][::-1]
        below = grid[i:]

        above = above[: len(below)]
        below = below[: len(above)]

        if above == below:
            return i

    return 0


def part1(data):
    ans = 0
    for block in data:
        grid = block.split("\n")

        row = find_mirror(grid)
        ans += row * 100

        col = find_mirror(list(zip(*grid)))
        ans += col

    return ans


def find_smudge(grid):
    for i in range(1, len(grid)):
        above = grid[:i][::-1]
        below = grid[i:]

        if (
            sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                for x, y in zip(above, below)
            )
            == 1
        ):
            return i

    return 0


def part2(data):
    ans = 0
    for block in data:
        grid = block.split("\n")

        row = find_smudge(grid)
        ans += row * 100

        col = find_smudge(list(zip(*grid)))
        ans += col

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
