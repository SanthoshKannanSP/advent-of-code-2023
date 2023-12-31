def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")
        
    return data

def part1(data):
    points = [(0, 0)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    b = 0

    for line in data:
        d, n, _ = line.split()
        dr, dc = dirs[d]
        n = int(n)
        b += n
        r, c = points[-1]
        points.append((r + dr * n, c + dc * n))

    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    i = A - b // 2 + 1

    return i + b

def part2(data):
    points = [(0, 0)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    b = 0

    for line in data:
        _, _, x = line.split()
        x = x[2:-1]
        dr, dc = dirs["RDLU"[int(x[-1])]]
        n = int(x[:-1], 16)
        b += n
        r, c = points[-1]
        points.append((r + dr * n, c + dc * n))

    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    i = A - b // 2 + 1

    return i + b

if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))