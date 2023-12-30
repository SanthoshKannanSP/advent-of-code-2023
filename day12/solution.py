from concurrent.futures import ProcessPoolExecutor


def load():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")

    return data


def count(config, nums):
    if config == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in config else 1

    result = 0
    if config[0] in ".?":
        result += count(config[1:], nums)

    if config[0] in "#?":
        if (
            nums[0] <= len(config)
            and "." not in config[: nums[0]]
            and (nums[0] == len(config) or config[nums[0]] != "#")
        ):
            result += count(config[nums[0] + 1 :], nums[1:])

    return result


def part1(data):
    ans = 0
    for line in data:
        config, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        ans += count(config, nums)

    return ans


def part2(data):
    ways = 0
    for row in data:
        record, checksum = row.split()
        checksum = [int(n) for n in checksum.split(",")]
        record = "?".join([record for i in range(5)])
        checksum *= 5
        positions = {0: 1}
        for i, contiguous in enumerate(checksum):
            new_positions = {}
            for k, v in positions.items():
                for n in range(
                    k, len(record) - sum(checksum[i + 1 :]) + len(checksum[i + 1 :])
                ):
                    if (
                        n + contiguous - 1 < len(record)
                        and "." not in record[n : n + contiguous]
                    ):
                        if (
                            i == len(checksum) - 1 and "#" not in record[n + contiguous :]
                        ) or (
                            i < len(checksum) - 1
                            and n + contiguous < len(record)
                            and record[n + contiguous] != "#"
                        ):
                            new_positions[n + contiguous + 1] = (
                                new_positions[n + contiguous + 1] + v
                                if n + contiguous + 1 in new_positions
                                else v
                            )
                    if record[n] == "#":
                        break
            positions = new_positions
        ways += sum(positions.values())
    return ways


if __name__ == "__main__":
    data = load()
    print(part1(data))
    print(part2(data))
