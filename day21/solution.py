from collections import deque

def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")
        
    return data


def part1(data):
    sr, sc = next((r, c) for r, row in enumerate(data) for c, ch in enumerate(row) if ch == "S")

    m,n = len(data),len(data[0])
    
    ans = set()
    visited = set([(sr, sc)])
    q = deque([(sr, sc, 64)])

    while q:
        r, c, s = q.popleft()

        if s % 2 == 0:
            ans.add((r, c))
        if s == 0:
            continue

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nr >= m or nc < 0 or nc >= n or data[nr][nc] == "#" or (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            q.append((nr, nc, s - 1))

    return len(ans)

def part2(data):
    sr, sc = next((r, c) for r, row in enumerate(data) for c, ch in enumerate(row) if ch == "S")

    m,n = len(data),len(data[0])
    steps = 26501365

    def fill(sr, sc, ss):
        ans = set()
        visited = set([(sr, sc)])
        q = deque([(sr, sc, ss)])

        while q:
            r, c, s = q.popleft()

            if s % 2 == 0:
                ans.add((r, c))
            if s == 0:
                continue

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if nr < 0 or nr >= m or nc < 0 or nc >= n or data[nr][nc] == "#" or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                q.append((nr, nc, s - 1))
        
        return len(ans)

    data_width = steps // m - 1

    odd = (data_width // 2 * 2 + 1) ** 2
    even = ((data_width + 1) // 2 * 2) ** 2

    odd_points = fill(sr, sc, m * 2 + 1)
    even_points = fill(sr, sc, m * 2)

    corner_t = fill(m - 1, sc, m - 1)
    corner_r = fill(sr, 0, m - 1)
    corner_b = fill(0, sc, m - 1)
    corner_l = fill(sr, m - 1, m - 1)

    small_tr = fill(m - 1, 0, m // 2 - 1)
    small_tl = fill(m - 1, m - 1, m // 2 - 1)
    small_br = fill(0, 0, m // 2 - 1)
    small_bl = fill(0, m - 1, m // 2 - 1)

    large_tr = fill(m - 1, 0, m * 3 // 2 - 1)
    large_tl = fill(m - 1, m - 1, m * 3 // 2 - 1)
    large_br = fill(0, 0, m * 3 // 2 - 1)
    large_bl = fill(0, m - 1, m * 3 // 2 - 1)

    return odd * odd_points + even * even_points + corner_t + corner_r + corner_b + corner_l + (data_width + 1) * (small_tr + small_tl + small_br + small_bl) + data_width * (large_tr + large_tl + large_br + large_bl)

if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))