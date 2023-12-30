def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def part1(data):
    neighbours = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }

    m = len(data)
    n = len(data[0])

    sr, sc = 0, 0

    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == "S":
                sr, sc = r, c
                break
        else:
            continue
        break

    p1, p2 = None, None

    adj = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
    for dx, dy in adj:
        cr, cc = sr + dx, sc + dy
        if 0 <= cr < m and 0 <= cc < n and data[cr][cc] in neighbours:
            pipe = data[cr][cc]
            for x, y in neighbours[pipe]:
                if cr + x == sr and cc + y == sc:
                    if p1 is None:
                        p1 = (cr, cc)
                    else:
                        p2 = (cr, cc)

    visited = set([(sr, sc)])

    def move(r, c):
        pipe = data[r][c]
        for x, y in neighbours[pipe]:
            if (r + x, c + y) not in visited:
                return (r + x, c + y)

    count = 1
    while p1 != p2:
        np1 = move(*p1)
        np2 = move(*p2)
        visited.add(p1)
        visited.add(p2)
        p1 = np1
        p2 = np2
        count += 1

    return count


def part2(data):
    neighbours = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }

    m = len(data)
    n = len(data[0])

    sr, sc = 0, 0

    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == "S":
                sr, sc = r, c
                break
        else:
            continue
        break

    p1, p2 = None, None

    adj = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
    for dx, dy in adj:
        cr, cc = sr + dx, sc + dy
        if 0 <= cr < m and 0 <= cc < n and data[cr][cc] in neighbours:
            pipe = data[cr][cc]
            for x, y in neighbours[pipe]:
                if cr + x == sr and cc + y == sc:
                    if p1 is None:
                        p1 = (cr, cc)
                    else:
                        p2 = (cr, cc)

    for pipe in neighbours:
        if (p1[0] - sr, p1[1] - sc) in neighbours[pipe] and (
            p2[0] - sr,
            p2[1] - sc,
        ) in neighbours[pipe]:
            data[sr] = data[sr].replace("S", pipe)
            break
    visited = set([(sr, sc)])

    def move(r, c):
        pipe = data[r][c]
        for x, y in neighbours[pipe]:
            if (r + x, c + y) not in visited:
                return (r + x, c + y)

    while p1 != p2:
        np1 = move(*p1)
        np2 = move(*p2)
        visited.add(p1)
        visited.add(p2)
        p1 = np1
        p2 = np2
    visited.add(p1)

    def count_intersects(i, j):
        line = data[i]
        count = 0
        for k in range(j):
            if not (i, k) in visited:
                continue
            count += line[k] in {"J", "L", "|"}
        return count

    ans = 0
    for r, row in enumerate(data):
        for c in range(n):
            if not (r, c) in visited:
                intersects = count_intersects(r, c)
                if intersects % 2 == 1:
                    ans += 1

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
