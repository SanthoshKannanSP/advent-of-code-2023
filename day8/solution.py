from collections import defaultdict
from functools import reduce


def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def part1(data):
    graph = defaultdict(dict)
    seq = data[0]
    n = len(seq)

    for line in data[2:]:
        source, dest = line.split(" = ")
        left, right = dest.lstrip("(").rstrip(")").split(", ")
        graph[source]["L"] = left
        graph[source]["R"] = right

    node = "AAA"
    dest = "ZZZ"
    step = 0

    while node != dest:
        index = step % n
        node = graph[node][seq[index]]
        step += 1

    return step


def part2(data):
    graph = defaultdict(dict)
    seq = data[0]
    n = len(seq)
    nodes = []

    for line in data[2:]:
        source, dest = line.split(" = ")
        left, right = dest.lstrip("(").rstrip(")").split(", ")
        graph[source]["L"] = left
        graph[source]["R"] = right
        if source[-1] == "A":
            nodes.append(source)

    def mapper(node, index):
        return graph[node][seq[index]]

    ans = []
    for node in nodes:
        step = 0
        while node[-1] != "Z":
            index = step % n
            node = mapper(node, index)
            step += 1
        ans.append(step)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, ans)


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
