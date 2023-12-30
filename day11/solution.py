def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def part1(data):
    m, n = len(data), len(data[0])

    galaxies = []
    for i in range(m):
        for j in range(n):
            if data[i][j] == "#":
                galaxies.append((i, j))

    N = len(galaxies)

    empty_row = [all([data[i][j] == "." for j in range(n)]) for i in range(m)]
    empty_col = [all([data[i][j] == "." for i in range(m)]) for j in range(n)]


    def dist(a, b):
        i1, j1 = a
        i2, j2 = b

        i1, i2 = min(i1, i2), max(i1, i2)
        j1, j2 = min(j1, j2), max(j1, j2)

        ans = 0
        for i in range(i1, i2):
            ans += 1
            if empty_row[i]:
                ans += 1
        for j in range(j1, j2):
            ans += 1
            if empty_col[j]:
                ans += 1

        return ans


    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            d = dist(galaxies[i], galaxies[j])
            ans += d

    return ans

def part2(lines):
    m, n = len(data), len(data[0])

    galaxies = []
    for i in range(m):
        for j in range(n):
            if data[i][j] == "#":
                galaxies.append((i, j))

    N = len(galaxies)

    empty_row = [all([data[i][j] == "." for j in range(n)]) for i in range(m)]
    empty_col = [all([data[i][j] == "." for i in range(m)]) for j in range(n)]


    def dist(a, b):
        i1, j1 = a
        i2, j2 = b

        i1, i2 = min(i1, i2), max(i1, i2)
        j1, j2 = min(j1, j2), max(j1, j2)

        ans = 0
        for i in range(i1, i2):
            ans += 1
            if empty_row[i]:
                ans += 10**6 - 1
        for j in range(j1, j2):
            ans += 1
            if empty_col[j]:
                ans += 10**6 - 1

        return ans


    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            d = dist(galaxies[i], galaxies[j])
            ans += d

    return ans


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))