from collections import Counter


def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def card(x, part1=True):
    if x.isnumeric():
        return int(x)

    return {"T": 10, "J": 11 if part1 else 1, "Q": 12, "K": 13, "A": 14}[x]


class Hand:
    def __init__(self, line, part1=True):
        hand, bid = line.split()
        self.hand = tuple(card(x, part1) for x in hand)
        self.bid = int(bid)
        self.type = self.get_type(part1)

    def get_type(self, part1):
        counter = Counter(self.hand)
        highest = 0
        if part1 is False:
            wilds = counter[1]
            del counter[1]
            highest += wilds
        if counter:
            highest += max(counter.values())

        if highest == 5:
            return 6
        if highest == 4:
            return 5
        if len(counter) == 2:
            return 4
        if highest == 3:
            return 3
        if len(counter) == 3:
            return 2
        if highest == 2:
            return 1
        return 0

    def __lt__(self, other):
        return self.type < other.type or (
            self.type == other.type and self.hand < other.hand
        )

    def __repr__(self):
        return f"{self.hand}"


def part1(data):
    hands = [Hand(i) for i in data]
    hands.sort()
    ans = 0
    for i, hand in enumerate(hands):
        ans += (i + 1) * hand.bid

    return ans


def part2(data):
    hands = [Hand(i, part1=False) for i in data]
    hands.sort()
    ans = 0
    for i, hand in enumerate(hands):
        ans += (i + 1) * hand.bid

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
