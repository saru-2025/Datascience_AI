# 🚗 Auto Driving Car Simulation

Welcome! This is a straightforward, human-readable Python simulation of autonomous cars navigating a 2D grid. Each car follows simple commands like turning and moving forward, while collisions and boundaries are properly handled.

---

## 📦 Project Structure

| File                   | What It's For                                                                 |
| ---------------------- | ----------------------------------------------------------------------------- |
| `main.py`            | Main interface – lets users create fields, add cars, and run the simulation. |
| `car.py`             | The Car class — manages direction, position, and command execution.          |
| `engine.py`          | Handles step-by-step simulation and detects collisions.                       |
| `test_simulation.py` | Automated test suite – covers all logic including edge cases.                |
| `README.md`          | Instructions --This guide explains how to run and test the application.       |

---

## ▶️ How to Run

From terminal, simply run:

```bash
python main.py
```

You’ll be guided step-by-step:

1. Define the field size
2. Add as many cars as you like (name, position, direction, commands)
3. Simulate all car movements step-by-step
4. View final positions or collision results

---

## 🧪 Running the Tests

To make sure everything works perfectly:

```bash
python -m unittest test_simulation.py
```

---

## ✅ What We are Testing

| Test Name                                | What It Checks                                         |
| ---------------------------------------- | ------------------------------------------------------ |
| `test_single_car_simple_path`          | A car moves correctly and ends in the expected place.  |
| `test_prevent_out_of_bounds`           | Car can't move off the grid — such moves are ignored. |
| `test_detect_collision_between_cars`   | Detects crash between two cars and logs both parties.  |
| `test_no_move_command`                 | Car with empty commands stays where it starts.         |
| `test_off_grid_starting_point`         | Handles oddball start positions gracefully.            |
| `test_multiple_collisions_possible`    | Several cars crashing at once? We’ve got it.          |
| `test_invalid_commands_ignored`        | Junk inputs like A, X, Z are safely ignored.           |
| `test_overlapping_start_position`      | Two cars on same starting tile = instant trouble.      |
| `test_unequal_command_lengths`         | One car might finish early — no problem.              |
| `test_circular_path_returns_to_origin` | Validates movement like “RFRFRFRF” ends at start.    |
| `test_no_cars_added`                   | Simulation behaves well even if no cars are added.     |
| `test_long_command_string`             | Stress-tested with 500+ move commands — no crashes.   |

---

## 💡 Developer Notes

- Only directions `N`, `E`, `S`, `W` are accepted
- Only commands `F`, `L`, `R` do something
- Cars freeze on collision
- Input validation is friendly but tight
- All logic is testable and modular

---

## 🔐 What’s Not Included

- No compiled binaries (`.exe`, `.dll`, etc.)
- No UI or database – pure console experience
- No third-party libraries needed
