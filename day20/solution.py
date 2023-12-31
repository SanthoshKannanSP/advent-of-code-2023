from collections import deque
import math

def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")
    
    return data

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}

def part1(data):
    modules = {}
    broadcast_targets = []

    for line in data:
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"

    lo, hi = 0,0

    for _ in range(1000):
        lo += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
        
        while q:
            origin, target, pulse = q.popleft()

            if pulse == "lo":
                lo += 1
            else:
                hi += 1
            
            if target not in modules:
                continue
            
            module = modules[target]
            
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

    return lo * hi

def part2(data):
    modules = {}
    broadcast_targets = []

    for line in data:
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"

    (feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

    cycle_lengths = {}
    seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

    presses = 0

    while True:
        presses += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
        
        while q:
            origin, target, pulse = q.popleft()
            
            if target not in modules:
                continue
            
            module = modules[target]
            
            if module.name == feed and pulse == "hi":
                seen[origin] += 1

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                else:
                    assert presses == seen[origin] * cycle_lengths[origin]
                    
                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = x * cycle_length // math.gcd(x, cycle_length)
                    return x
            
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))