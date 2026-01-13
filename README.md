## Why a calculator?
As a first portfolio project a calculator was well within the scope of my capabilities.

I wanted a project which I could use to demonstrate my ability to code, this was the choice because it is complex enough to show the level of proficiency I have while also not being easy to understand.

## What I did:
I made a calculator that does calculations from left to right with no order of operations

To avoid input problems, the inputs are based on the buttons that the software makes and the user clicks instead of keyboard inputs(so no, typing with the number pad or number keys will not work)

## What I learned:
I learned the importance and importance of how to name functions and variables

I learned about extracting functions to improve functionality, readability, and workability 

While coding I ran into functions I did not use, so I learned to only add functions once you have a specific need for them

I learned after completion that floating point math can cause strange unintended consequences in many programming languages.

I also added a user interface and made the run_calculator_gui.py runable from the command line.
If you wish to run the program from the command line(cmd), replace "run_calculator_gui.py" with the path to where that file is saved.
```
python run_calculator_gui.py
```
## There is always room for improvement

#### If I did this project over, some changes to how the program works could be:
I would change the use of floating points as a default storage method to avoid floating point issues by storing whole numbers and decimals separately.

To more easily allow the program to be improved in the future, the buttons being coded in manually would be redone to take the operations which can be performed and assigning them each individually using a key(dictionary) of which inputs result in what happening.

The names on the buttons can be somewhat confusing and are hard coded into the program. I would improve this by letting the names be more freely assigned in the program and choosing better names for the text on the buttons that the user sees.

I would shorten the button_writes_to_backend function by extracting out how to identify each situation and what to do in each situation into separate functions. This would improve readability and ease of understanding drastically by removing the need to sift through complicated logic and a scroll.

I would keep the apply_no_order_of_operations function and add the option to use order of operations by having a separate function to handle the how the computer chooses what to do in sequence.

#### Additions
I would add single character removal

Then, I would add the ability to change where the cursor is located and the ability to move it 

Type hints, more comments, and better comments explaining how things should work would be added so anyone reading the code can more easily understand the decisions made and why things are the way they are

Finally, I would build a function to give the option to calculate with order of operations or without at the user's choice

