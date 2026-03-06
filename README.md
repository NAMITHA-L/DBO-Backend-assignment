# Rover Navigation System – Digital Back Office Backend Assignment

## Overview

This project implements a Python-based simulation of robotic rovers navigating a rectangular plateau.
Each rover receives a sequence of movement commands and updates its position accordingly while respecting plateau boundaries.

The program processes rover instructions sequentially and outputs the final position and orientation of each rover.

---

## Project Structure

```
DBO-Backend-assignment
│
├── main.py
├── input.txt
├── .gitignore
│
└── src
    └── rover.py
```

**File Responsibilities**

| File           | Purpose                                                             |
| -------------- | ------------------------------------------------------------------- |
| `main.py`      | Entry point. Handles input reading, validation, and rover execution |
| `src/rover.py` | Contains the `Rover` class and movement logic                       |
| `input.txt`    | Input data containing plateau size, rover positions, and commands   |
| `.gitignore`   | Prevents unnecessary system and compiled files from being committed |

---

## How to Run

### Requirements

* Python 3.x

### Execution

Run the program from the project root directory:

```bash
python main.py input.txt
```

The program reads the rover instructions from the provided file and prints the final rover positions to the console.

---

## Input Format

The input file follows this structure:

```
<plateau_x> <plateau_y>
<x> <y> <direction>
<command_sequence>
<x> <y> <direction>
<command_sequence>
```

### Example Input

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

### Expected Output

```
1 3 N
5 1 E
```

---

## Design Decisions

### Object-Oriented Design

A `Rover` class was used to encapsulate rover state and behavior.
This keeps movement logic separate from input/output handling.

### Separation of Concerns

The application separates responsibilities:

* `main.py` → program orchestration and validation
* `rover.py` → rover navigation logic

This improves maintainability and readability.

### Command Mapping

A movement map dictionary translates rover direction into coordinate changes.

```
N → (0, +1)
E → (+1, 0)
S → (0, -1)
W → (-1, 0)
```

This approach avoids complex conditional logic and keeps movement computation simple.

### Direction Rotation

Rover rotation uses a circular direction list:

```
['N', 'E', 'S', 'W']
```

Index arithmetic with modulo ensures correct wrapping when turning left or right.

---

## Safety Features

### Plateau Boundary Protection

The rover only moves if the next position is within plateau limits.

```
0 ≤ x ≤ plateau_x
0 ≤ y ≤ plateau_y
```

This prevents invalid rover positions.

### Command Validation

Only the following commands are accepted:

```
L → Turn Left
R → Turn Right
M → Move Forward
```

Invalid commands raise a `ValueError`.

### Initial Position Validation

Rover starting coordinates are validated to ensure they lie within the plateau.

### File Handling

The program safely handles missing input files using exception handling.

---

## Assumptions

* The plateau's lower-left corner is `(0, 0)`
* Rovers execute sequentially
* Each rover has exactly one instruction line
* Commands consist only of `L`, `R`, and `M`

---

## Possible Extensions

Potential improvements for a production system include:

* Rover collision detection
* Logging instead of console output
* Support for multiple input formats
* Unit testing for rover movement logic
* Asynchronous Processing: Implementing asyncio to handle multiple rovers moving concurrently in real-time.(async - wont wait for one async task to complete, instead runs other task)

---

## Author

Namitha
Backend Developer Internship Assignment – Digital Back Office
