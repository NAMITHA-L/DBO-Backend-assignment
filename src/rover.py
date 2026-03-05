class Rover:
    directions = ['N', 'E', 'S', 'W']

    move_map = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        idx = Rover.directions.index(self.direction)
        self.direction = Rover.directions[(idx - 1) % 4]

    def turn_right(self):
        idx = Rover.directions.index(self.direction)
        self.direction = Rover.directions[(idx + 1) % 4]

    def move(self):
        dx, dy = Rover.move_map[self.direction]
        self.x += dx
        self.y += dy

    def execute(self, commands):
        for cmd in commands:
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'M':
                self.move()

    def get_position(self):
        return f"{self.x} {self.y} {self.direction}"