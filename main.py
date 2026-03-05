import sys
from src.rover import Rover


def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
    plateau_x, plateau_y = map(int, lines[0].split())

    i = 1
    results = []

    while i < len(lines):
        x, y, direction = lines[i].split()
        x, y = int(x), int(y)

        commands = lines[i + 1]

        rover = Rover(x, y, direction, plateau_x, plateau_y)
        rover.execute(commands)

        results.append(rover.get_position())

        i += 2

    for r in results:
        print(r)


if __name__ == "__main__":
    main()