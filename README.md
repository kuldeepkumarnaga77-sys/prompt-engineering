# prompt-engineering
# Class Average

A small Python script that takes student scores, computes the class average, and counts how many students scored strictly above that average.

## Requirements

- Python 3.8 or later
- No third-party packages

## Project layout

```
cursor/
  messy.py                          # score calculations and CLI output
  output.txt                        # sample report from an earlier run
  .cursor/rule/python-standards.mdc # local Cursor coding rules
```

## How it works

`students` maps each name to a numeric score. The script then:

1. Collects the scores into a list
2. Computes the mean with `class_average`
3. Counts scores strictly greater than that mean with `count_above_average`
4. Prints both results

Empty score lists return `0` instead of dividing by zero.

## Run

From the `cursor` folder:

```bash
python messy.py
```

Expected output for the built-in sample data:

```text
Class average: 80.00
Students above average: 3
```

Alice (88), Charlie (95), and Eve (81) are above the average of 80. Bob (72) and Dana (64) are not.

## Change the data

Edit the `students` dictionary in `messy.py`:

```python
students = {
    "Alice": 88,
    "Bob": 72,
    "Charlie": 95,
    "Dana": 64,
    "Eve": 81,
}
```

Then run the script again.

## Coding conventions

This repo uses Cursor rules in `cursor/.cursor/rule/python-standards.mdc`:

- Descriptive variable names (single letters only for loop counters)
- One-line docstring on every function stating what it returns
- f-strings for output
- Named constants instead of repeating magic numbers
- No unused imports
- No extra features beyond what was asked
