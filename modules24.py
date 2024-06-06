# A module is a file that contains python statement and definations and can be called in another file
#so with module,you can create a function or variable in one file and export and use in another file

# import nine24
# nine24.my_function_second()

# nine24.my_function("wale")

# import nine24 as fl
# import math,time
# print(math.ceil(5.444))
# print(math.floor(5.999))
# print(math.cos(30))
# current_time =time.time()

# formate_timw=time. (time)
# print(math.tan(45))
# print(time.timzone)
# print(time.time())

# current_time = time,time

# fl.my_function(first_name="Olawale", last_name="Omoyeni")

# from nine24 import my_function

# my_function(first_name="Olawale", last_name="Omoyeni")




#Module Creation:
#Task: Create a module named calculator with functions for addition, subtraction, multiplication, and division.
#Tips: Highlight code structure, function definitions, and return values.
#Challenge: Add error handling for invalid inputs.
#Module Import and Use:
#Task: Write a program that imports the calculator module and uses its functions to perform calculations.
#Tips: Guide students through import, function calls, and parameter passing.
#Challenge: Allow calculations with multiple variables and user input.#


#Module Creation:
#Task: Create a module named calculator with functions for addition, subtraction, multiplication, and division.
#Tips: Highlight code structure, function definitions, and return values.
#Challenge: Add error handling for invalid inputs.
#Module Import and Use:
#Task: Write a program that imports the calculator module and uses its functions to perform calculations.
#Tips: Guide students through import, function calls, and parameter passing.
#Challenge: Allow calculations with multiple variables and user input.#

from nine24 import addition, division, multiplication, subtraction

def first_input():
  message = 0
  while message < 3: 
   t = 0
   y = input("Enter your first Number: ")
   for x in y:
    if x.isdigit():
      continue   
    else:
      t = 1
      break
   
   if t == 1:
     if message != 2:
      print("Please try again")
     message += 1
   else:
    message += 4
  if t == 1:
    return None
  else:
    return int(y)
#   else:
#    print('This input is invalid, try again')
#    first_input()

def second_input():
  message = 0
  while message < 3: 
   t = 0
   y = input("Enter your second Number: ")
   for x in y:
    if x.isdigit():
      continue   
    else:
      t = 1
      break
   
   if t == 1:
     if message != 2:
      print("Please try again")
     message += 1
   else:
    message += 4
  if t == 1:
    return None
  else:
    return int(y)

 
firstuserInput = first_input()

if firstuserInput != None:
  seconduserInput = second_input()
  if seconduserInput != None:

   operation = input("Please specify what operation do you want to perform on these numbers either (add, subtract, divide, multiply): ")
   operation = operation.lower()
   if operation == "add":   
    print("The result is: ",addition(firstuserInput, seconduserInput))
   elif operation == "subtract":
    print("The result is: ", subtraction(firstuserInput, seconduserInput))
   elif operation == "divide":
    print("The result is: ", division(firstuserInput, seconduserInput))
   elif operation == "multiply":
    print("The result is: ", multiplication(firstuserInput, seconduserInput))
   else:
    print("Invalid operation")

  else:
   print("End of program")  

else:
  print("End of program")
