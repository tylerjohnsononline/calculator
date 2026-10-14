![image](https://github.com/tylerjohnsononline/calculator/blob/gui_colors/images/calculator_with_color.png)
![image](https://github.com/tylerjohnsononline/calculator/blob/gui_colors/images/working_calculator_example.png)

### How To Use
Step 1: Download this repository and Python if you haven't already (make sure to install Python):  https://www.python.org/downloads/

Step 2: Run the following command: 

```
python -m venv place_to_place_virtual_environment
```

Step 3: Open the virtual environment:

```
place_to_place_virtual_environment\Scripts\activate.bat
```

```
pip install -r requirements.txt
```

```
python run_calculator_gui.py
```
Step 4: Use the window that looks like calculator image by clicking on the numbers and operations you want to perform.

Step 5: Click the "=" button when your equation is ready.

## Why a calculator?
I wanted a first project which I could use to demonstrate my ability to code.  A calculator was well within the scope of my capabilities while being complex enough to show significant proficiency.

## What I learned:
I learned the importance of functions and variables, and how to name them.

I learned about extracting functions to improve functionality, readability, and workability.

While coding this calculator, I was presented with function options that I decided didn't add value to my project goal.  I learned how to keep my code streamlined by omitting extraneous functions.

I learned after completion that floating point math can cause strange unintended consequences in many programming languages, see below for what I would have done differently.

I also learned about adding command line functionality by adding a user interface and made the run_calculator_gui.py executable from the command line.
If you wish to run the program from the command line (cmd), replace "run_calculator_gui.py" with the path to where that file is saved.
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

