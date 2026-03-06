import sys
from src.rover import Rover


def main():

    # Check command line argument
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Handle missing file
    try:
        with open(input_file) as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Plateau size
    plateau_x, plateau_y = map(int, lines[0].split())

    i = 1
    results = []

    while i < len(lines):

        x, y, direction = lines[i].split()
        x, y = int(x), int(y)

        # Validate initial rover position
        if not (0 <= x <= plateau_x and 0 <= y <= plateau_y):
            raise ValueError(
                f"Invalid starting position: ({x}, {y}) is outside the plateau."
            )

        commands = lines[i + 1]

        rover = Rover(x, y, direction, plateau_x, plateau_y)

        rover.execute(commands)

        results.append(rover.get_position())

        i += 2

    for r in results:
        print(r)


if __name__ == "__main__":
    main()