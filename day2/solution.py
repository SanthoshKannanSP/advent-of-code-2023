def part1(data):
    total = {"red": 12, "green": 13, "blue": 14}
    s = 0
    for line in data:
        game, sets = line.split(":")
        _, game_id = game.split()
        balls = [
            ball.split()
            for single_set in sets.split("; ")
            for ball in single_set.split(", ")
        ]
        for number, color in balls:
            if int(number) > total[color]:
                break
        else:
            s += int(game_id)

    return s


def part2(data):
    s = 0
    for line in data:
        game, sets = line.split(":")
        _, game_id = game.split()
        balls = [
            ball.split()
            for single_set in sets.split("; ")
            for ball in single_set.split(", ")
        ]
        required = {"red": 0, "green": 0, "blue": 0}
        for number, color in balls:
            required[color] = max(required[color], int(number))
        s += required["red"] * required["blue"] * required["green"]
    return s


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

    print(part1(data))
    print(part2(data))
