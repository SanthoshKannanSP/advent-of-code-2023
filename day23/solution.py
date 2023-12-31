from collections import defaultdict

def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")
        
    return data

def part1(data):
    m,n = len(data),len(data[0])
    
    start = (0, data[0].index("."))
    end = (m - 1, data[-1].index("."))

    points = [start, end]

    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and data[nr][nc] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))

    graph = defaultdict(dict)

    dirs = {
        "^": [(-1, 0)],
        "v": [(1, 0)],
        "<": [(0, -1)],
        ">": [(0, 1)],
        ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    }

    for sr, sc in points:
        stack = [(0, sr, sc)]
        visited = set([(sr, sc)])

        while stack:
            count, r, c = stack.pop()
            
            if count != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = count
                continue

            for dr, dc in dirs[data[r][c]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and data[nr][nc] != "#" and (nr, nc) not in visited:
                    stack.append((count + 1, nr, nc))
                    visited.add((nr, nc))

    visited = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        visited.add(pt)
        for nx in graph[pt]:
            if nx not in visited:
                m = max(m, dfs(nx) + graph[pt][nx])
        visited.remove(pt)

        return m

    return dfs(start)

def part2(data):
    m, n= len(data),len(data[0])
    
    start = (0, data[0].index("."))
    end = (m - 1, data[-1].index("."))

    points = [start, end]

    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and data[nr][nc] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))

    graph = defaultdict(dict)

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            count, r, c = stack.pop()
            
            if count != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = count
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and data[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((count + 1, nr, nc))
                    seen.add((nr, nc))

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    return dfs(start)

if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))