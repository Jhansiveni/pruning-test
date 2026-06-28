# Alpha-Beta Pruning Algorithm in Python

## Overview

This project demonstrates the **Alpha-Beta Pruning** algorithm, an optimization of the **Minimax** algorithm used in Artificial Intelligence for decision-making in two-player games.

The algorithm reduces the number of nodes evaluated in the game tree by eliminating branches that cannot influence the final decision, making the search process faster while producing the same optimal result as Minimax.

---

## Features

- Simple and beginner-friendly Python implementation
- Recursive Alpha-Beta Pruning algorithm
- Supports MAX and MIN player turns
- Demonstrates pruning using Alpha and Beta values
- Returns the optimal decision value
- Easy to understand and modify

---

## Algorithm

1. Start from the root node.
2. Alternate between MAX and MIN players.
3. Update:
   - **Alpha** → Best value found so far for MAX.
   - **Beta** → Best value found so far for MIN.
4. If **Alpha ≥ Beta**, prune the remaining branches.
5. Continue until leaf nodes are reached.
6. Return the optimal value.

---

## Project Structure

```
alpha-beta-pruning/
│
├── alphabeta.py
└── README.md
```

---

## Sample Input

```python
values = [10, 9, 14, 18, 5, 4, 50, 3]
```

---

## Sample Output

```
Optimal Value = 10
```

---

## Time Complexity

| Case | Complexity |
|------|------------|
| Worst Case | O(b^d) |
| Best Case (with pruning) | O(b^(d/2)) |

Where:

- **b** = Branching factor
- **d** = Depth of the game tree

---

## Space Complexity

```
O(d)
```

where **d** is the depth of the recursion tree.

---

## Applications

- Chess engines
- Tic-Tac-Toe AI
- Connect Four
- Checkers
- Game-playing AI
- Decision-making systems

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/alpha-beta-pruning.git
```

2. Navigate to the project folder

```bash
cd alpha-beta-pruning
```

3. Run the Python file

```bash
python alphabeta.py
```

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Learning Objectives

This project helps in understanding:

- Game Trees
- Minimax Algorithm
- Alpha-Beta Pruning
- Recursive Programming
- AI Search Algorithms

---

## Author

**Jhansiveni Desu**

---

## License

This project is open-source and available for educational purposes.
