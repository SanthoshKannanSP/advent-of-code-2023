from os import getresuid


def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def part1(data):
    data = list(map("".join, zip(*data)))
    data = [
        "#".join(
            ["".join(sorted(list(group), reverse=True)) for group in row.split("#")]
        )
        for row in data
    ]
    data = list(map("".join, zip(*data)))

    return sum(row.count("O") * (len(data) - r) for r, row in enumerate(data))


def cycle(data):
    for _ in range(4):
        data = tuple(map("".join, zip(*data)))
        data = tuple(
            "#".join(
                ["".join(sorted(list(group), reverse=True)) for group in row.split("#")]
            )
            for row in data
        )
        data = tuple(row[::-1] for row in data)

    return data


def part2(data):
    data = tuple(data)
    visited = set(data)
    array = [data]

    index = 0

    while True:
        index += 1
        data = cycle(data)
        if data in visited:
            break
        visited.add(data)
        array.append(data)

    first = array.index(data)

    data = array[(1000000000 - first) % (index - first) + first]

    return sum(row.count("O") * (len(data) - r) for r, row in enumerate(data))


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
