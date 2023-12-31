from collections import deque


def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def solve(data, r, c, dr, dc):
    visited = set()
    q = deque([(r, c, dr, dc)])
    m, n = len(data), len(data[0])
    while q:
        r, c, dr, dc = q.popleft()

        r, c = r + dr, c + dc

        if r < 0 or r >= m or c < 0 or c >= n:
            continue

        ch = data[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))

        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))

        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))

        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

    coords = {(r, c) for (r, c, _, _) in visited}

    return len(coords)


def part1(data):
    return solve(data, 0, -1, 0, 1)


def part2(data):
    ans = 0
    m, n = len(data), len(data[0])

    for r in range(m):
        ans = max(ans, solve(data, r, -1, 0, 1))
        ans = max(ans, solve(data, r, n, 0, -1))

    for c in range(n):
        ans = max(ans, solve(data, -1, c, 1, 0))
        ans = max(ans, solve(data, m, c, -1, 0))

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
