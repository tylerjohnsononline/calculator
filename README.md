### How To Use
step 1: download this repository and python if you haven't already(make sure to install python):https://www.python.org/downloads/

step 2: run the following command: 

```
python -m venv place_to_place_virtual_environment
```

step 3: open the virtual environment:

```
place_to_place_virtual_environment\Scripts\activate.bat
```

```
pip install -r requirements.txt
```

```
python run_calculator_gui.py
```
step 4: use the window that looks like calculator image by clicking on the numbers and operations you want to perform.

step 5: click the "=" button when your equation is ready.

## Why a calculator?
As a first portfolio project a calculator was well within the scope of my capabilities.

I wanted a project which I could use to demonstrate my ability to code, this was the choice because it is complex enough to show the level of proficiency I have.

## What I did:
I made a calculator that does calculations from left to right with no order of operations.

To avoid input problems, the inputs are based on the buttons that the software makes and the user clicks instead of keyboard inputs(so no, typing with the number pad or number keys will not work).

## What I learned:
I learned the importance of and how to name functions and variables.

I learned about extracting functions to improve functionality, readability, and workability.

While coding I ran into functions I did not use, so I learned to only add functions after finding a specific use case.

I learned after completion that floating point math can cause strange unintended consequences in many programming languages, see bellow for what I would have done differently.

I also learned about adding command line functionality by adding a user interface and made the run_calculator_gui.py executable from the command line.
If you wish to run the program from the command line(cmd), replace "run_calculator_gui.py" with the path to where that file is saved.
```
python run_calculator_gui.py
```
## There is always room for improvement

#### If I did this project over, some changes to how the program works could be:
I would change the use of floating points as a default storage method to avoid floating point issues by storing whole numbers and decimals separately.

To improve maintainability, the buttons could be keyed to different functions.

The names on the buttons can be somewhat confusing and are hard coded into the program. I would improve this by letting the names be more freely assigned in the program and choosing better names for the text on the buttons that the user sees.

I would shorten the button_writes_to_backend function by extracting out how to identify each situation and what to do in each situation into separate functions. This would improve readability and ease of understanding drastically by removing the need to sift through complicated logic and a scroll.

I would keep the apply_no_order_of_operations function and add the option to use order of operations by having a separate function to handle the how the computer chooses what to do in sequence.

#### Potential Additions 
Add single character removal.

Add the ability to move the cursor.

Build a function to give the option to calculate with order of operations.

For developers and maintainance, in the code: Type hints, more comments, and better comments explaining how things should work would be added so anyone reading the code can more easily understand the decisions made and why things are the way they are.



