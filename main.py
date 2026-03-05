import sys
from src.rover import Rover


def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]

    plateau_x, plateau_y = map(int, lines[0].split())

    i = 1
    results = []

    while i < len(lines):
        x, y, direction = lines[i].split()
        x, y = int(x), int(y)

        commands = lines[i + 1]

        rover = Rover(x, y, direction)
        rover.execute(commands)

        results.append(rover.get_position())

        i += 2

    for r in results:
        print(r)


if __name__ == "__main__":
    main()