from collections import *


def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def part1(data):
    ans = 0
    for line in data:
        _, cards = line.split(": ")
        winning, own = cards.split(" | ")
        winning = set(winning.split())
        own = own.split()

        points = 0
        for card in own:
            if card in winning:
                points = points << 1 if points != 0 else 1

        ans += points

    return ans


def part2(data):
    count = defaultdict(int)
    ans = 0
    for index, line in enumerate(data):
        _, cards = line.split(": ")
        winning, own = cards.split(" | ")
        winning = set(winning.split())
        own = own.split()

        points = 0
        for card in own:
            if card in winning:
                points += 1
        if points > 0:
            for i in range(index + 1, index + points + 1):
                count[i] += count[index] + 1
        ans += count[index] + 1
    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
