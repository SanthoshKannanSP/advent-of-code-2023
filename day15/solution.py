def load():
    with open("input.txt", "r") as f:
        data = f.read().strip()

    return data


def hash(s):
    ans = 0
    for ch in s:
        ans += ord(ch)
        ans *= 17
        ans %= 256

    return ans


def part1(data):
    return sum(map(hash, data.split(",")))


def part2(data):
    boxes = [[] for _ in range(256)]
    focal = dict()

    for s in data.split(","):
        if "-" in s:
            label = s[:-1]
            index = hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = s.split("=")
            length = int(length)
            index = hash(label)
            if label not in boxes[index]:
                boxes[index].append(label)

            focal[label] = length

    ans = 0

    for i, box in enumerate(boxes, 1):
        for j, label in enumerate(box, 1):
            ans += i * j * focal[label]

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
