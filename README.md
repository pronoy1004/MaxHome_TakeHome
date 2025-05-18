## MaxHome_TakeHome
Repo for the take home assignment given by MaxHome AI, and my rather simple solution to explore Europa

## How to run


```bash
python3 europa.py
```

## Example Inputs and Outputs

### Input

```
(no input)
```

**Output**

```
Error: No input data
```

---

### Input

```
5 5
8 8 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

**Output**

```
Error: Invalid Plateau Dimensions
```

---

### Input

```
5 5
1 2 N
LMLMLMLMM
3 3 E
```

**Output**

```
Error: Invalid number of robot lines
```

---

### Input

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

**Output**

```
1 3 N
5 1 E
```

---

### Input

```
5 5
1 2 S
LMLMLMLMM
3 3 E
MMRMMRMRRMMMMMMMMMMMMMMM
```

**Output**

```
1 1 S
6 1 Robot Out of Bounds
```

---

### Input

```
15 15
1 2 N
LMLMLMLMMMMMMLMRMRMRM
3 3 E
MMRMMRMRRM
3 4 S
LMLMLMLMM
3 3 E
MMRMMRMRRM
1 2 S
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

**Output**

```
1 7 S
5 1 E
3 3 S
5 1 E
1 1 S
5 1 E
```

## Assumptions

* Each line is comma-separated in code but logically represents a space-separated input line.
* I have assumed that the robots can navigate around each other or be in the same coordinates (no collisions happen).
* Only `L`, `R`, and `M` are valid commands.
* Plateau dimensions and robot positions are integers.
* Since the robots execute sequentially, if any one of the robots goes out of bounds, the function exits at that point resulting in all the subsequent robots to not move.