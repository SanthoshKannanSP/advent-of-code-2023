def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return [i for i in data if i]


class Range:
    def __init__(self, lower, upper, offset=0):
        self.lower = lower
        self.upper = upper
        self.offset = offset

    def intersect(self, other):
        temp = Range(
            max(self.lower, other.lower), min(self.upper, other.upper), self.offset
        )
        if temp.lower < temp.upper:
            return temp
        return None

    def subtract(self, other):
        ins = self.intersect(other)
        if ins is None:
            return [Range(self.lower, self.upper)]

        if ins.lower == self.lower and ins.upper == self.upper:
            return []

        if ins.lower == self.lower:
            return [Range(ins.upper, self.upper)]

        if ins.upper == self.upper:
            return [Range(self.lower, ins.lower)]

        return [Range(self.lower, ins.lower), Range(ins.upper, self.upper)]

    def move(self):
        self.lower = self.lower + self.offset
        self.upper = self.upper + self.offset


class Mapper:
    def __init__(self, line, data):
        self.ranges = []
        n = len(data)

        while line < n and not data[line][0].isdigit():
            line += 1

        while line < n and data[line][0].isdigit():
            dest, source, count = [int(i) for i in data[line].split()]
            self.ranges.append((source, dest, count))
            line += 1

        self.line = line

    def map(self, value):
        for source, dest, count in self.ranges:
            if source <= value < source + count:
                return dest + (value - source)
        return value


class Range_mapper:
    def __init__(self, line, data):
        self.ranges = []
        n = len(data)

        while line < n and not data[line][0].isdigit():
            line += 1

        while line < n and data[line][0].isdigit():
            dest, source, count = [int(i) for i in data[line].split()]
            self.ranges.append(Range(source, source + count - 1, dest - source))
            line += 1
        self.line = line

    def map(self, other):
        ans = []
        for r in self.ranges:
            n = len(other)
            for _ in range(n):
                interval = other.pop(0)
                ins = r.intersect(interval)
                if ins is not None:
                    ins.move()
                    ans.append(ins)
                sub = interval.subtract(r)
                for i in sub:
                    other.append(i)

        for i in other:
            ans.append(i)

        return ans


def part1(data):
    _, seeds = data[0].split(": ")
    seeds = [int(i) for i in seeds.split()]
    line = 1

    seed_soil = Mapper(line, data)
    soils = [seed_soil.map(seed) for seed in seeds]
    line = seed_soil.line
    del seed_soil

    soil_fert = Mapper(line, data)
    ferts = [soil_fert.map(soil) for soil in soils]
    line = soil_fert.line
    del soil_fert

    fert_water = Mapper(line, data)
    waters = [fert_water.map(fert) for fert in ferts]
    line = fert_water.line
    del fert_water

    water_light = Mapper(line, data)
    lights = [water_light.map(water) for water in waters]
    line = water_light.line
    del water_light

    light_temp = Mapper(line, data)
    temps = [light_temp.map(light) for light in lights]
    line = light_temp.line
    del light_temp

    temp_hum = Mapper(line, data)
    hums = [temp_hum.map(temp) for temp in temps]
    line = temp_hum.line
    del temp_hum

    hum_loc = Mapper(line, data)
    locs = [hum_loc.map(hum) for hum in hums]
    line = hum_loc.line
    del hum_loc

    return min(locs)


def part2(data):
    _, seeds = data[0].split(": ")
    seeds = [int(i) for i in seeds.split()]
    line = 1
    seeds = [Range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    seed_soil = Range_mapper(line, data)
    soils = seed_soil.map(seeds)
    line = seed_soil.line
    del seed_soil

    soil_fert = Range_mapper(line, data)
    ferts = soil_fert.map(soils)
    line = soil_fert.line
    del soil_fert

    fert_water = Range_mapper(line, data)
    waters = fert_water.map(ferts)
    line = fert_water.line
    del fert_water

    water_light = Range_mapper(line, data)
    lights = water_light.map(waters)
    line = water_light.line
    del water_light

    light_temp = Range_mapper(line, data)
    temps = light_temp.map(lights)
    line = light_temp.line
    del light_temp

    temp_hum = Range_mapper(line, data)
    hums = temp_hum.map(temps)
    line = temp_hum.line
    del temp_hum

    hum_loc = Range_mapper(line, data)
    locs = hum_loc.map(hums)
    line = hum_loc.line
    del hum_loc

    return min([i.lower for i in locs])


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
