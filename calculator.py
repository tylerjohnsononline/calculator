def run_operation(first_number, operation_string, second_number):
  first_number = float(first_number)
  second_number = float(second_number)
  if operation_string == "+" : calculation_output = first_number + second_number
  if operation_string == "-" : calculation_output = first_number - second_number
  if operation_string == "*" : calculation_output = first_number * second_number
  if operation_string == "/" and second_number != 0 : 
    calculation_output = first_number / second_number
  elif operation_string == "/" and second_number == 0 : 
    calculation_output = 'undefined'

  if calculation_output % 1 == 0:
    calculation_output = int(calculation_output)

  return calculation_output


def count_places_right_of_decimal(self, where):
      number = repr(float(self.backend[where]))
      right_of_decimal = number.split('.')
      decimal_num = right_of_decimal[1].rstrip('0')

      places = len(decimal_num) 
      return places

def count_places_left_of_decimal(self, where):
      number = repr(float(self.backend[where]))
      right_of_decimal = number.split('.')
      decimal_num = right_of_decimal[0].lstrip('0')

      places = len(decimal_num) 
      return places

def apply_no_order_of_operations(copy_interpereted_list): #this is to say, none
  # if only a number was passed through returns that to be the answer
  if len(copy_interpereted_list) == 1:
    return float(copy_interpereted_list[0])
  # calculate_left_to_right is as the name suggests
  else:
    return calculate_left_to_right(copy_interpereted_list)


def equate(inputed_list):
  computer_interoperable_list = make_interpereted_list(inputed_list)

  if check_number_formatted_for_backend(computer_interoperable_list) is True:
    result = apply_order_of_operations(computer_interoperable_list)
    if isinstance(result, float):
      if result%1 == 0:
        result = int(result)
  elif check_number_formatted_for_backend(computer_interoperable_list) is False: 
    result = 'format your numbers properly please'

  above_buttons_show_result(computer_interoperable_list, result)
  return result


def write_after_decimal(self, number:int, where:int):
    last_non_zero_place = count_places_right_of_decimal(self, where)
    tens_place = (10 ** (self.trailing_zeros[where] + last_non_zero_place + 1))
    self.backend[where] += number / tens_place
    self.trailing_zeros[where] = 0


class NumberOperatorOrder:
  def __init__(self, backend_list, leading_zeros,
               trailing_zeros, is_negative,
               previous_answer):
    self.backend = backend_list
    self.leading_zeros = leading_zeros
    self.trailing_zeros = trailing_zeros
    self.is_negative = is_negative
    self.previous_answer = previous_answer

  def write_whole_number(self, number_to_write, where):
    if self.is_negative[where] == True:
      number_to_write = number_to_write * (-1)
    if isinstance(self.backend[where], int):
      self.backend[where] = self.backend[where]*10 + number_to_write
    elif isinstance(self.backend[where], float):
      write_after_decimal(self, number_to_write, where)


  def write_decimal(self, where):
    self.backend[where] = float(self.backend[where])

  def write_leading_zero(self, where):
    self.leading_zeros[where] += 1
  def delete_leading_zero(self, where):
    if self.leading_zeros[where] > 0: 
      self.leading_zeros[where] -= 1

  def write_trailing_zero(self, where):
    self.trailing_zeros[where] += 1
  def delete_trailing_zero(self, where):
    if self.trailing_zeros[where] > 0: 
      self.trailing_zeros[where] -= 1
  

  def write_operator(self, operator):
    if len(self.backend) < 2:
      pass
    elif is_there_an_operator(self.backend[-1]):
      self.backend[-1] = operator
    else:
      self.backend.append('')
      self.backend[-1] = operator
  
  def answer_with_no_operations(self):
    self.previous_answer = [self.backend[0]]
  def calculate_left_to_right(self):
    name = self.backend
    last_operator_location = len(name) - name[::-1].index(name[-1]) - 1


    import numpy as np
    track_operator_list = np.arange(1,last_operator_location, 2)

    # run calculation for each operator left to right
    for x in track_operator_list:
      if x == 1:
        equals = run_operation(name[x - 1], name[x], name[x + 1])
      else:
        equals = run_operation(equals, name[x], name[x + 1])
    self.previous_answer = self.previous_answer + [equals]

  def number_times_minus_one(self, where):
    self.backend[-1] = self.backend[-1] * -1
  def plus_minus(self, where):
    self.is_negative[-1] ^= True
  
  def add_space_to_place_info(self):
    self.backend = self.backend + [0]
    self.leading_zeros = self.leading_zeros  + [0]
    self.trailing_zeros = self.trailing_zeros + [0]
    self.is_negative = self.is_negative + [False]

  # def edit_backspace
  def clear(self):
    self.backend = []
    self.leading_zeros = []
    self.trailing_zeros = []
    self.is_negative = []
  def delete_space_to_place_info(self):
    if len(self.backend) > 0:
      self.backend = self.backend[:-1]
      self.leading_zeros = self.leading_zeros[:-1]
      self.trailing_zeros = self.trailing_zeros[:-1]
      self.is_negative = self.is_negative[:-1]
    elif len(self.backend) == 0:
      self.backend = []
      self.leading_zeros = []
      self.trailing_zeros = []
      self.is_negative = []

storage = NumberOperatorOrder([], [], [], [], [''])


def is_there_an_operator(es) :
  for rew in ['+', '-', '*', '/']:
    if rew == es:
      return True 
  return False
def one_through_nine_list_of_strings():
  string_numbers = []
  for hey in range(1, 10):
    string_numbers += [str(hey)]
  return string_numbers
def assign_inputs_to_backgroud_readible_form():
  numbers = {'0':0, '1':1, '2':2, '3':3, '4':4,
             '5':5, '6':6, '7':7, '8':8, '9':9}
  operations = {'+':'+', '-':'-', '*':'*', '/':'/'}
  return numbers, operations
def button_writes_to_backend(command ="0", editing_list = storage, extra = False):
  input_numbers, operators = assign_inputs_to_backgroud_readible_form()
  
  # write a nonzero, single digit integer to the end of a number

  if command in one_through_nine_list_of_strings():
    new_number = input_numbers[command]
    if editing_list.backend == []: 
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = new_number

    elif isinstance(editing_list.backend[-1], int):
      editing_list.write_whole_number(new_number, -1)

    elif isinstance(editing_list.backend[-1], float):
      editing_list.write_whole_number(new_number, -1)

    elif isinstance(editing_list.backend[-1], str):
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = new_number

  # write a zero so it can be seen
  if command == '0':
    new_number = input_numbers[command]
    if editing_list.backend == []: 
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = new_number
      editing_list.write_leading_zero(editing_list, -1)

    elif isinstance(editing_list.backend[-1], int):
      if editing_list.backend[-1] == 0 :
        editing_list.write_leading_zero( -1)
      else:
        editing_list.write_whole_number(new_number, -1)

    elif isinstance(editing_list.backend[-1], float):
      editing_list.write_trailing_zero(-1)

    elif isinstance(editing_list.backend[-1], str):
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = new_number
      editing_list.write_trailing_zero(-1)

  # write a new operator to the backend or overwrite the last operator
  if command in operators:
    operation = operators[command]
    if editing_list.backend == []: 
      pass

    elif isinstance(editing_list.backend[-1], int):
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = operation

    elif isinstance(editing_list.backend[-1], float):
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = operation

    elif isinstance(editing_list.backend[-1], str):
      editing_list.backend[-1] = operation

  # handle positive negative switch from a string input of '+/-'
  if command == '+/-':
    if editing_list.backend == []: 
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = 0
      editing_list.plus_minus(-1)

    elif isinstance(editing_list.backend[-1], int):
      editing_list.number_times_minus_one(-1)
      editing_list.plus_minus(-1)

    elif isinstance(editing_list.backend[-1], float):
      editing_list.number_times_minus_one(-1)
      editing_list.plus_minus(-1)

    elif isinstance(editing_list.backend[-1], str):
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = 0
      editing_list.plus_minus(-1)
  
  # write decimals when appropriate
  if command == '.':
    if editing_list.backend == []: 
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = 0.0

    elif isinstance(editing_list.backend[-1], int):
      editing_list.write_decimal(-1)

    elif isinstance(editing_list.backend[-1], float):
      pass

    elif isinstance(editing_list.backend[-1], str):
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = 0.0
  
  # clear the whole list inputted by the user
  if command == 'clear':
    editing_list.clear()
  
  # calculate with the list input by the user
  if command == '=':
    if len(editing_list.backend) == 1:
      editing_list.answer_with_no_operations()
    elif len(editing_list.backend) % 2 == 0 :
      pass
    else:
      editing_list.calculate_left_to_right()
  
  # put the previous calculation's result as an input
  if command == "ANSWER":
    if editing_list.previous_answer[-1] == '':
      pass
    elif editing_list.backend == []: 
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = editing_list.previous_answer[-1]
    elif isinstance(editing_list.backend[-1], int):
      pass
    elif isinstance(editing_list.backend[-1], float):
      pass
    elif editing_list.backend[-1] in operators:
      editing_list.add_space_to_place_info()
      editing_list.backend[-1] = editing_list.previous_answer[-1]
  
  # remove a number or operator
  if command == "back":
    editing_list.delete_space_to_place_info()

#   update_typing_on_screen(storage)
#   update_answer_on_screen(editing_list.previous_answer[-1])


#front end user inputs grid

"""


grid_down = 5
grid_across = 4
# grid

#1-9 and 0, in calculator fashion

# put numbers 1 through 9 on buttons
# put 0, decimal, and equals sign on buttons

for i in range(3):
   for j in range(3):
        number_operator_grid[i, j] = create_button(f'{numerals}', '')
        if numerals in check: numerals += 1

number_operator_grid[i+1,j-1] = create_button('0', '')
number_operator_grid[i+1,j-2] = create_button('.', '')
number_operator_grid[i+1,j] = create_button('=', '')

# makes and assigns buttons to the 4 basic operators
operator_standing_by = ['/', '*', '-', '+']
for i in range(4): 
  number_operator_grid[i,3] = create_button(f'{operator_standing_by[i]}', '')

# makes buttons for the previous answer, clear, flip
number_operator_grid[i+1,j-1] = create_button("ANSWER", '')
number_operator_grid[i+1,j-2] = create_button('+/-', '')
number_operator_grid[i+1,j] = create_button('back', '')
number_operator_grid[i+1,j-3] = create_button('clear', '')
"""
