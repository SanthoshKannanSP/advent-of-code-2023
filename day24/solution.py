import sympy

def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")
        
    return data

class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        
        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy

def part1(data):
    hailstones = [Hailstone(*list(map(int, line.replace("@", ",").split(",")))) for line in data]

    ans = 0

    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]:
            a1, b1, c1 = hs1.a, hs1.b, hs1.c
            a2, b2, c2 = hs2.a, hs2.b, hs2.c
            if a1 * b2 == b1 * a2:
                continue
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hs1, hs2)):
                    ans += 1

    return ans

def part2(data):
    hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in data]

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

    equations = []

    for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            break
        
    ans = answers[0]

    return ans[xr] + ans[yr] + ans[zr]

if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))