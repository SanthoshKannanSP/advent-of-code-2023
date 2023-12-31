from heapq import heappush, heappop

def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")
        
    return data

def part1(data):
    data = [list(map(int, line.strip())) for line in data]
    m, n = len(data),len(data[0])

    visited = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, count = heappop(pq)
        
        if r == m-1 and c == n-1:
            return hl

        if (r, c, dr, dc, count) in visited:
            continue

        visited.add((r, c, dr, dc, count))
        
        if count < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n:
                heappush(pq, (hl + data[nr][nc], nr, nc, dr, dc, count + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < m and 0 <= nc < n:
                    heappush(pq, (hl + data[nr][nc], nr, nc, ndr, ndc, 1))
                    
def part2(data):
    data = [list(map(int, line.strip())) for line in data]
    m, n = len(data),len(data[0])

    visited = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, count = heappop(pq)
        
        if r == m-1 and c == n-1 and count>=4:
            return hl

        if (r, c, dr, dc, count) in visited:
            continue

        visited.add((r, c, dr, dc, count))
        
        if count < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n:
                heappush(pq, (hl + data[nr][nc], nr, nc, dr, dc, count + 1))

        if count>=4 or (dr,dc)==(0,0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < m and 0 <= nc < n:
                        heappush(pq, (hl + data[nr][nc], nr, nc, ndr, ndc, 1))
    
                    
if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))