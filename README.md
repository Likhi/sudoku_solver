## What is this?

I just wanted to solve sudoku puzzles. But it's probably an over-done challenge.
So I converted a good one from Python 2 to Python 3 with some tools and, "yay!" I can solve sudoku puzzles.

## Maybe run these

python -m venv .venv 
^if that doesn't work the first time, run it again, maybe add on a 'sudo' or maybe run it in PowerShell.

.venv\scripts\activate

python -m pip install --upgrade pip

## Then, definitely run this:

python -m pip install -r requirements.txt

## Now what?

Run the script using:
python solve_script.py
python solve_script.py grid1
python solve_script.py challenge1
python solve_script.py 003020600900305001001806400008102900700000008006708200002609500800203009005010300
python solve_script.py ...6..4..7....36......91.8...........5.18...3...3.6.45.4.2...6.9.3.......2....1..

## Anything else?

You can look up the grid options in grids.py.