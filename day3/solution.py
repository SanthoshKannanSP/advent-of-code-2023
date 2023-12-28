from collections import defaultdict


def load():
    with open("./input.txt", "r") as f:
        data = f.readlines()
    data = [line.strip("\n") for line in data]
    return data


def part1(data):
    lines = len(data)
    adj = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
    ans = 0

    for row in range(lines):
        number = ""
        keep = False
        chars = len(data[row])
        for col in range(chars):
            if data[row][col].isdigit():
                number += data[row][col]
                if not keep:
                    for dx, dy in adj:
                        if (
                            row + dx in range(lines)
                            and col + dy in range(chars)
                            and data[row + dx][col + dy] != "."
                            and not data[row + dx][col + dy].isdigit()
                        ):
                            keep = True

            else:
                if len(number) > 0 and keep:
                    ans += int(number)
                number = ""
                keep = False
        if len(number) > 0 and keep:
            ans += int(number)
    return ans


def part2(data):
    lines = len(data)
    adj = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
    ans = 0
    d = defaultdict(list)

    for row in range(lines):
        chars = len(data[row])
        star = (-1, -1)
        number = ""
        for col in range(chars):
            if data[row][col].isdigit():
                number += data[row][col]

                for dx, dy in adj:
                    if (
                        row + dx in range(lines)
                        and col + dy in range(chars)
                        and data[row + dx][col + dy] == "*"
                    ):
                        star = (row + dx, col + dy)

            else:
                if star[0] != -1:
                    d[star].append(int(number))
                number = ""
                star = (-1, -1)
        if star[0] != -1:
            d[star].append(int(number))

    for numbers in d.values():
        if len(numbers) == 2:
            ans += numbers[0] * numbers[1]

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
