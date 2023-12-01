with open("input.txt","r") as f:
    data = f.readlines()

def part1():
    s = 0
    for line in data:
        l = line.strip()
        n = len(l)
        num = ""
        
        for i in range(n):
            if l[i].isdigit():
                num+=l[i]
                break
        
        for i in range(n-1,-1,-1):
            if l[i].isdigit():
                num+=l[i]
                break
        s+=int(num)
        
    return s
    
def part2():
    d = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "zero":0
    }

    s = 0
    for line in data:
        l = line.strip()
        n = len(l)
        num = ""
        temp = ""
        for i in range(n):
            if l[i].isdigit():
                num+=l[i]
                break
            temp+=l[i]
            for j in d:
                if j in temp:
                    num+=str(d[j])
                    break
            else:
                continue
            break
        
        temp=""
        for i in range(n-1,-1,-1):
            if l[i].isdigit():
                num+=l[i]
                break
            temp = l[i]+temp
            for j in d:
                if j in temp:
                    num+=str(d[j])
                    break
            else:
                continue
            break

        s += int(num)
    
    return s

if __name__=="__main__":
    print(part1())
    print(part2())