print("it's kulvir here")   # where print is function 
"Python is a programming language that allows you to write code to perform various tasks."
"Python is case-sensitive, meaning that 'Variable' and 'variable' are considered different identifiers."
"Python is a high-level language, meaning that it abstracts away many low-level details, allowing you to focus on writing code without worrying about memory management or hardware specifics."
"Python is an interpreted language, meaning that you can run Python code directly without the need for compilation, making it easy to test and debug your code."
"Python is dynamically typed, meaning that you don't need to declare the data type of a variable explicitly; the interpreter infers the type based on the value assigned to the variable."
"Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming, allowing you to choose the style that best suits your needs."
"Python has a large standard library that provides many built-in functions and modules, making it easy to perform common tasks without having to write everything from scratch."
"Python is widely used in various fields, including web development, data analysis, machine learning, scientific computing, and automation, making it a versatile language for many applications."
"Python has a large and active community, which means there are many resources available for learning, troubleshooting, and sharing code with others."
"Python is known for its readability and simplicity, making it an excellent choice for beginners and experienced programmers alike."
"Python is open-source, meaning that its source code is freely available, and you can contribute to its development or use it in your projects without any licensing fees."
"Python is a versatile language that can be used for a wide range of applications, from simple scripts to complex web applications and data analysis tasks."
"Python is a popular programming language known for its simplicity and readability, making it an excellent choice for beginners and experienced developers alike."  


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#What is variable?
# A variable is a name that refers to a value. it can change its value.
name="kulvir"
age=20
print(name,age)

#Now let's create another variable and store the existing variable
name2 = name
print(name2)  # This will print the value of name2, which is "kulvir"

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------


#Rules for Identifiers commonly known as variable names and can be called as functions.
# 1. Variable names can only contain letters, numbers, and underscores.
# 2. Variable names cannot start with a number.
# 3. Identifiers can be the combination of uppercase and lowercase letters and can be of any length.
# For example, these are valid identifiers:
user_name = "Alice"
userAge = 25
_user_id = 12345
user123 = "Bob"

# 4. Identifiers cannot be a reserved keyword in Python (like 'if', 'else', 'while', etc.).
myVariable = 10  # Valid variable name
print_name = "Hello"  # Valid variable name
your_first_name = "Kulvir"  # Valid variable name

# 5. it cannot contain special characters like @, #, $, %, etc.
# Identifier cannot start with a digit. Some examples of invalid variable names:
# 1st_variable = 5  # Invalid variable name (starts with a digit)
# my-variable = 10  # Invalid variable name (contains a hyphen)
# my variable = 10  # Invalid variable name (contains a space)

# 6. Variable names are case-sensitive, meaning 'myVariable' and 'myvariable' are different variables.
MyVariable = 20  # Valid variable name, different from myVariable
variable_1 = 30  # Valid variable name
variable1= 40  # Valid variable name

# 7. Variable names should be descriptive and meaningful to improve code readability.
# For example, instead of using 'x' or 'y', use 'user_age' or 'product_price'.
user_age = 30  # Descriptive variable name
product_price = 19.99  # Descriptive variable name
print(user_age,product_price)
# 8. Variable names should be simple, short and meaningful.


#-----------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Python Data Types
#1. Integers
# Integers are whole numbers, both positive and negative, without any decimal point.
integer_number = 42
negative_integer = -7
print("Integer Number:", integer_number)
print("Negative Integer:", negative_integer)
#2. Floats
# Floats are numbers that have a decimal point, representing real numbers.
float_number = 3.14
negative_float = -2.5
print("Float Number:", float_number)
print("Negative Float:", negative_float)
#3. Strings
# Strings are sequences of characters enclosed in single or double quotes.
string_text = "Hello, World!"
single_quote_string = 'Python is fun!'
print("String Text:", string_text)
print("Single Quote String:", single_quote_string)
#4. Booleans
# Booleans represent truth values, either True or False.
boolean_true = True
boolean_false = False
print("Boolean True:", boolean_true)
print("Boolean False:", boolean_false)
#5. Lists
# Lists are ordered collections of items, which can be of different data types.
list_of_numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, True]
print("List of Numbers:", list_of_numbers)
print("Mixed List:", mixed_list)
#6. Tuples
# Tuples are similar to lists but are immutable (cannot be changed after creation).
tuple_of_numbers = (1, 2, 3)
mixed_tuple = (1, "two", 3.0, True)
print("Tuple of Numbers:", tuple_of_numbers)
print("Mixed Tuple:", mixed_tuple)
#7. Dictionaries
# Dictionaries are collections of key-value pairs, where each key is unique.
dictionary_example = {
    "name": "Kulvir",
    "age": 20,
    "is_student": True
}
print("Dictionary Example:", dictionary_example)
#8. Sets
# Sets are unordered collections of unique items.
set_of_numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "two", 3.0, True}
print("Set of Numbers:", set_of_numbers)
print("Mixed Set:", mixed_set)

#-----------------------------------------------------------------------------------------------------

# Python Variables and Data Types
# Variables are used to store data values, and Python has various built-in data types to handle
# different kinds of data. Here are some common data types in Python:
# 1. Integers: Whole numbers, both positive and negative.
integer_var = 10
# 2. Floats: Numbers with decimal points.
float_var = 3.14
# 3. Strings: Sequences of characters enclosed in single or double quotes.
string_var = "Hello, World!"
# 4. Booleans: Represents True or False values.
boolean_var = True
# 5. Lists: Ordered collections of items, which can be of different data types.
list_var = [1, 2, 3, "four", 5.0]
# 6. Tuples: Similar to lists but immutable (cannot be changed after creation).
tuple_var = (1, 2, 3, "four", 5.0)
# 7. Dictionaries: Collections of key-value pairs, where each key is unique.
#8. Sets: Unordered collections of unique items.
dictionary_var = {
    "name": "Kulvir",
    "age": 20,
    "is_student": True
}
set_var = {1, 2, 3, 4, 5}
# Printing the variables and their types
print("Integer Variable:", integer_var, "Type:", type(integer_var))
print("Float Variable:", float_var, "Type:", type(float_var))
print("String Variable:", string_var, "Type:", type(string_var))
print("Boolean Variable:", boolean_var, "Type:", type(boolean_var))
print("List Variable:", list_var, "Type:", type(list_var))
print("Tuple Variable:", tuple_var, "Type:", type(tuple_var))
print("Dictionary Variable:", dictionary_var, "Type:", type(dictionary_var))
print("Set Variable:", set_var, "Type:", type(set_var))

#-----------------------------------------------------------------------------------------------------

"print(type(name))  # This will print the type of the variable 'name', which is a string"
"print(type(name))  # This will print the type of the variable 'name', which is a string"
"print(type(age))   # This will print the type of the variable 'age', which is an integer"

#Common primary data types in Python:
# 1. int: Represents integers (whole numbers).
# 2. float: Represents floating-point numbers (numbers with decimal points).
# 3. str: Represents strings (sequences of characters).
# 4. bool: Represents boolean values (True or False).
# 5. none: Represents the absence of a value or a null value.

example_int = 42
example_float = 3.14
example_str = "Hello, Python!"
example_bool = True
example_none = None
print("Example Integer:", example_int, "Type:", type(example_int))
print("Example Float:", example_float, "Type:", type(example_float))
print("Example String:", example_str, "Type:", type(example_str))
print("Example Boolean:", example_bool, "Type:", type(example_bool))
print("Example None:", example_none, "Type:", type(example_none))



#-----------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------


#Keywords in Python
# Keywords are reserved words in Python that have special meanings and cannot be used as variable names.
import keyword
print("Python Keywords:")   
for kw in keyword.kwlist:
    print(kw)             
"# This will print all the keywords in Python, which are reserved and cannot be used as variable names."
#-----------------------------------------------------------------------------------------------------
"# These keywords are used to define control flow, functions, classes, and other structures in Python."
"# For example, 'if', 'else', 'while', 'for', 'def', 'class', etc. are all keywords in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('if'))  # This will print True, indicating that 'if' is a keyword in Python."
#"print(keyword.iskeyword('my_variable'))  # This will print False, indicating that 'my_variable' is not a keyword in Python."
#"print(keyword.iskeyword('class'))  # This will print True, indicating that 'class' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('function'))  # This will print False, indicating that 'function' is not a keyword in Python."
#"print(keyword.iskeyword('def'))  # This will print True, indicating that 'def' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('while'))  # This will print True, indicating that 'while' is a keyword in Python."
#"print(keyword.iskeyword('for'))  # This will print True, indicating that 'for' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('import'))  # This will print True, indicating that 'import' is a keyword in Python."
#"print(keyword.iskeyword('from'))  # This will print True, indicating that 'from' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('as'))  # This will print True, indicating that 'as' is a keyword in Python."
#"print(keyword.iskeyword('return'))  # This will print True, indicating that 'return' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('lambda'))  # This will print True, indicating that 'lambda' is a keyword in Python."
#"print(keyword.iskeyword('try'))  # This will print True, indicating that 'try' is a keyword in Python."
#"print(keyword.iskeyword('except'))  # This will print True, indicating that 'except' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('finally'))  # This will print True, indicating that 'finally' is a keyword in Python."
#"print(keyword.iskeyword('with'))  # This will print True, indicating that 'with' is a keyword in Python."
#"print(keyword.iskeyword('assert'))  # This will print True, indicating that 'assert' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('pass'))  # This will print True, indicating that 'pass' is a keyword in Python."
#"print(keyword.iskeyword('break'))  # This will print True, indicating that 'break' is a keyword in Python."
#"print(keyword.iskeyword('continue'))  # This will print True, indicating that 'continue' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('del'))  # This will print True, indicating that 'del' is a keyword in Python."
#"print(keyword.iskeyword('global'))  # This will print True, indicating that 'global' is a keyword in Python."
#"print(keyword.iskeyword('nonlocal'))  # This will print True, indicating that 'nonlocal' is a keyword in Python."
#-----------------------------------------------------------------------------------------------------
#"print(keyword.iskeyword('raise'))  # This will print True, indicating that 'raise' is a keyword in Python."
#"print(keyword.iskeyword('yield'))  # This will print True, indicating that 'yield' is a keyword in Python."
#"print(keyword.iskeyword('async'))  # This will print True, indicating that 'async' is a keyword in Python."
#"print(keyword.iskeyword('await'))  # This will print True, indicating that 'await' is a keyword in Python."



#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


#Print sum of two numbers

"Print sum of two numbers"
def sum_of_two_numbers(a, b):
    return a + b
# Example usage
result = sum_of_two_numbers(5, 10)
print("Sum of 5 and 10 is:", result)
#-----------------------------------------------------------------------------------------------------
a=4
b=3
sum = a + b
print(sum)
#or
print("Sum of", a, "and", b, "is:", sum)


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


#Comments in Python
# Types of comments in Python:
# 1. Single-line comments: Start with a hash symbol (#) and continue until the end of the line.
# 2. Multi-line comments: Enclosed in triple quotes (""" or ''') and can span multiple lines.
# 3. Inline comments: Placed on the same line as a statement, after the code, and preceded by a hash symbol (#).

#------------------------------------------------------------------------------------------------------
# 4. Docstrings: Special type of multi-line comment used to document functions, classes, and modules.
# 5. Docstrings are enclosed in triple quotes (""" or ''') and are used to describe the purpose and usage of the code.
# 6. They are often used as documentation for the code and can be accessed using the __doc__ attribute.
# 7. Example of docstring
def example_function():
    """This is an example function that does nothing."""
    pass
# 8.  You can access the docstring using the __doc__ attribute.
print(example_function.__doc__)  # This will print the docstring of the function.    
# 9. Output: This is an example function that does nothing.
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

# 1. Comments are used to explain code and make it more readable. They are ignored by the Python interpreter.
# 2. This is a single-line comment in Python
# 3. It starts with a hash symbol (#) and continues until the end of the line.
# 4. Multi-line comment
""" This is a multi-line comment in Python."""
# 5. It starts and ends with triple quotes (""" or ''') and can span multiple lines.
# 6. Comments can be used to explain complex code, provide context, or temporarily disable code during development.
# 7. Shortcut for commenting all the lines in a block is to select the lines and press Ctrl + / (or Command + / on Mac).


#------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
#Types of Operators in Python
# 1. Arithmetic Operators: Used for mathematical operations like addition, subtraction, multiplication, and division.
# 2. Comparison/Relational Operators: Used to compare values and return a boolean result (True or False).
# 3. Logical Operators: Used to combine conditional statements and return a boolean result.
# 4. Assignment Operators: Used to assign values to variables.
# 5. Bitwise Operators: Used to perform bit-level operations on integers.
# 6. Membership Operators: Used to check if a value is present in a sequence (like lists, tuples, or strings).
# 7. Identity Operators: Used to check if two variables point to the same object in memory.

#------------------------------------------------------------------------------------------------------
"Operator vs Operand"
#example:
# In the expression 'a + b', '+' is the operator, and 'a' and 'b' are the operands.
# 1. Operator: '+'
# 2. Operand: 'a' and 'b'
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
#1. Example of Arithmetic Operators
a = 10
b = 5
sum_result = a + b  # Addition
difference_result = a - b  # Subtraction
product_result = a * b  # Multiplication
quotient_result = a / b  # Division
modulus_result = a % b  # Modulus (remainder)
exponent_result = a ** b  # Exponentiation (a raised to the power of b)
floor_division_result = a // b  # Floor Division (quotient without remainder)
print("Arithmetic Operators:")
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Modulus:", modulus_result)
print("Exponent:", exponent_result)
print("Floor Division:", floor_division_result)

#------------------------------------------------------------------------------------------------------
#2. Example of Comparison/Relational Operators
is_equal = (a == b)  # Equal to
is_not_equal = (a != b)  # Not equal to
is_greater = (a > b)  # Greater than
is_less = (a < b)  # Less than
is_greater_equal = (a >= b)  # Greater than or equal to
is_less_equal = (a <= b)  # Less than or equal to
print("\nComparison Operators:")
print("Is Equal:", is_equal)
print("Is Not Equal:", is_not_equal)
print("Is Greater:", is_greater)
print("Is Less:", is_less)
print("Is Greater Equal:", is_greater_equal)
print("Is Less Equal:", is_less_equal)

#------------------------------------------------------------------------------------------------------
#3. Example of Logical Operators
is_true = True
is_false = False
and_result = is_true and is_false  # Logical AND
or_result = is_true or is_false  # Logical OR
not_result = not is_true  # Logical NOT
print("\nLogical Operators:")
print("AND Result:", and_result)
print("OR Result:", or_result)
print("NOT Result:", not_result)

#------------------------------------------------------------------------------------------------------
#4. Example of Assignment Operators
x = 10  # Assignment
x += 5  # Add and assign (x = x + 5)
x -= 3  # Subtract and assign (x = x - 3)
x *= 2  # Multiply and assign (x = x * 2)
x /= 2  # Divide and assign (x = x / 2)
x %= 3  # Modulus and assign (x = x % 3)
x **= 2  # Exponentiation and assign (x = x ** 2)
x //= 2  # Floor division and assign (x = x // 2)
print("\nAssignment Operators:")
print("Final Value of x:", x)

#------------------------------------------------------------------------------------------------------
#5. Example of Bitwise Operators
bit_a = 10  # Binary: 1010
bit_b = 4   # Binary: 0100
bitwise_and = bit_a & bit_b  # Bitwise AND
bitwise_or = bit_a | bit_b  # Bitwise OR
bitwise_xor = bit_a ^ bit_b  # Bitwise XOR
bitwise_not = ~bit_a  # Bitwise NOT
bitwise_left_shift = bit_a << 2  # Left shift
bitwise_right_shift = bit_a >> 2  # Right shift
print("\nBitwise Operators:")
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT:", bitwise_not)
print("Left Shift:", bitwise_left_shift)
print("Right Shift:", bitwise_right_shift)

#------------------------------------------------------------------------------------------------------
#6. Example of Membership Operators
my_list = [1, 2, 3, 4, 5]
is_member = 3 in my_list  # Check if 3 is in the list
is_not_member = 6 not in my_list  # Check if 6 is not in the list
print("\nMembership Operators:")
print("Is 3 a member of the list?", is_member)
print("Is 6 not a member of the list?", is_not_member)

#------------------------------------------------------------------------------------------------------
#7. Example of Identity Operators
a = [1, 2, 3]
b = a  # b is a reference to the same list as a
is_same = (a is b)  # Check if a and b are the same object
is_not_same = (a is not b)  # Check if a and b are not the same object
c = [1, 2, 3]  # c is a different object with the same content as a
is_c_same = (a is c)  # Check if a and c are the same object
is_c_not_same = (a is not c)  # Check if a and c are not the same object
print("\nIdentity Operators:")
print("Is a the same object as b?", is_same)
print("Is a not the same object as b?", is_not_same)
print("Is a the same object as c?", is_c_same)
print("Is a not the same object as c?", is_c_not_same)
#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
"Inshort all examples"
# 1. Arithmetic Operators
a=10
b=5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus (remainder)
print(a ** b)  # Exponentiation (a raised to the power of b) such as a^b

#2. Comparison/Relational Operators
a=10
b=50
print(a == b)  #False
print(a != b)  #True
print(a > b)   #False
print(a < b)   #True
print(a >= b)  #False
print(a <= b)  #True

#3. Assignment Operators
num=10
num=num+10 #10+10 = 20
#or
num += 10  # This is equivalent to num = num + 10
print(num)  # Output: 20

#-------------------------------------------------------------------------------------------------------
num =10
num *=3 # This is equivalent to num = num * 3
print("num:", num)  # Output: 30

num /= 2  # This is equivalent to num = num / 2
"the last value of num is 30, so 30 divided by 2 gives 15.0"
print("num:", num)  # Output: 15.0

num %= 4  # This is equivalent to num = num % 4
"the last value of num is 15.0, so 15.0 divided by 4 gives a remainder of 3.0"
print("num:", num)  # Output: 3.0 => IT IS REMAINDER VALUE

num **= 2  # This is equivalent to num = num ** 2
"the last value of num is 3.0, so 3.0 raised to the power of 2 is 9.0"
print("num:", num)  # Output: 9.0 => 3.0^2 = 9.0
#--------------------------------------------------------------------------------------------------------

#4. Logical Operators(not, and, or)
print(True and False)  # Output: False
print(True and True)   # Output: True
print(False and True)  # Output: False
print(False and False) # Output: False
print(True or False)   # Output: True
print(False or True)   # Output: True
print(False or False)  # Output: False
print(True or True)    # Output: True
print(not True)         # Output: False
print(not False)        # Output: True

#-------------------------------------------------------------------------------------------------------
"For examples easy to understand"
a=10
b=20
print(a > 5 and b < 30)  # Output: True (both conditions are true)
print(a < 5 or b > 15)   # Output: True (at least one condition is true)
print(not (a < 5))       # Output: True (the condition is false, so not makes it true)
print(not (b > a))  # Output: False (the condition is true, so not makes it false)
print (not (a == b))  # Output: True (the condition is false, so not makes it true)
print (not False)  # Output: True (not makes False true)
print (not True)  # Output: False (not makes True false)


val1=True
val2=True
print("and operator:", val1 and val2)  # Output: True (both values are True)
"if both values true in OR then it will return true otherwise it will return false if one is false"
print("or operator:", val1 or val2)    # Output: True (at least one value is True)

#we can use expressions here given below
print("or operator:", (val1 or val2) and (val1!=val2))  # Output: True (at least one value is True)
#make sure use brackets or parenthesis to avoid confusion in complex expressions
#------------------------------------------------------------------------------------------------------
val3=True
val4=False
print("and operator:", val3 and val4)  # Output: False (one value is False)
print("or operator:", val3 or val4)    # Output: True (at least one value is True)

#we can use expressions here given below
print("or operator:", (val3 or val4) and (val3!=val4))  # Output: True (at least one value is True)
#make sure use brackets or parenthesis to avoid confusion in complex expression
#in OR if both were false then it will return false

print("not operator:", val3==val4 and not val3)  # Output: False (val3 is True, so not val3 is False)
print("not operator:", not val3)  # Output: False (not makes True false
#------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------
#Types of Conversion in Python
"one is type conversion and other is type casting"
"Type Conversion: Automatically converting one data type to another by Python interpreter."
"Type Casting: Manually converting one data type to another using built-in functions like int(), float(), str(), etc." #zabardasti
#-------------------------------------------------------------------------------------------------------
#1. Example of Type Conversion
a=2 # Integer
b=3.4 # Float
c=a+b  # Python automatically converts 'a' to float for addition
print(c)  # Output: 5.4 (float)

#2. Example of Type Casting
a = 5  # Integer
b = 2.5  # Float
c = int(b)  # Manually converting float to integer
#why we are converting float to integer because we want to discard the fractional part
e=a+c # This will convert 'b' to an integer, discarding the fractional par
print(c)  # Output: 2 (integer, fractional part is discarded)
print(e)  # Output: 7 (integer addition)
#see how easy it is to convert float to integer

#3. Example of Type Casting with Strings
str_num = "10"  # String representation of a number
#we can convert string to integer using int() function
num = int(str_num)  # Manually converting string to integer
print(num)  # Output: 10 (integer)

#4. Example of Type Casting with Floats
str_float = "3.14"  # String representation of a float
#we can convert string to float using float() function
float_num = float(str_float)  # Manually converting string to float
print(float_num)  # Output: 3.14 (float)

#-------------------------------------------------------------------------------------------------------
#5. Example of Type Casting with Lists
list_str = ["1", "2", "3"]  # List of strings
#we can convert list of strings to list of integers using list comprehension
#with th help of list comprehension we can convert each string to integer
#we can take any variable name here, it can be x or y or z
#here we are using x as variable name
int_list = [int(x) for x in list_str]  # Manually converting each string to integer
list_me=[int(x) for x in list_str if int(x) > 1]  # Filtering and converting
#used conditional statement to filter out values greater than 1
print(list_me)  # Output: [2, 3] (list of integers greater than 1)
#we can also use filter function to filter out values greater than 1
int_list = list(filter(lambda x: int(x) > 1, list_str))  # Filtering and converting
print(int_list)  # Output: [2, 3] (list of integers greater than 1)
#using filter function to filter out values greater than 1
print(int_list)  # Output: [1, 2, 3] (list of integers)
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#WE CAN DO TYPE CASTING WHEN THERE IS AN VALID INTEGER OR NUMBER IS PRESENT IN THE STRING OR NEEDS TO BE CONVERTED
#EXAMPLE:
#1. Example of Type Casting with Strings
str_num = "10"  # String representation of a number
#we can convert string to integer using int() function
num = int(str_num)  # Manually converting string to integer
print(num)  # Output: 10 (integer)
#-------------------------------------------------------------------------------------------------------
#2. Example of Type Casting with Floats
str_float = "3.14"  # String representation of a float
#we can convert string to float using float() function
float_num = float(str_float)  # Manually converting string to float
print(float_num)  # Output: 3.14 (float)
#---------------------------------------------------------------------------------------------------------------------  

#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------


#---------------------HOW TO CONCATENATE STRINGS IN PYTHON-----------------------------------------------------------------
a=10
a=str(a)
b=str(2.5)  # Converting float to string
c=a+b # Concatenating strings
#because a is 10 and b is 2.5, the result will be "102.5" as strings after concatenation
#concatenation means joining two strings together
print(c) # Output: "102.5" (string)
#-----------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------HOW TO TAKE INPUTS FROM USERS------------------------------------------------------------
input("Enter your name: ")  # This will prompt the user to enter their name
#the input() function in python is used to take input from the user
#-----------------------------------------------------------------------------
#or you can use it like this
print("Hello, " + input("Enter your name: "))  # This will greet the user with their name
#it will concatenate the string "Hello, " with the user's input
#result of input is always a string
#-----------------------------------------------------------------------------------------------------------------------------------
int_a=input("Enter an integer: ")  
print(type(int_a), int_a)  # This will print the type of the input and the input itself
#whenever we try to take input from the user using input() function, it will always return a string
#either it is an integer or float or string, it will always return a string
#so if you want to convert it to integer you have to use int() function
#so if you want to convert it to float you have to use float() function
#-----------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------
#example of converting input to integer
int_a = int(input("Enter an integer: "))
#just surround the input() function with int() function
print(type(int_a), int_a)  # This will print the type of the input and the input itself
#now it will return an integer instead of a string
#-----------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------
#basically developers write programs like this adding int() or float() around input() function for performing proper operations
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Converting input to integer
marks = float(input("Enter your marks: "))  # Converting input to float 
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
#-----------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------LETS PRACTICE OUR PROGRAMS-------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
"WRITE A PROGRAM TO INPUT TWO NUMBERS AND PRINT THEIR SUM"
num1 = int(input("Enter first number: "))  # Taking input and converting to integer
num2 = int(input("Enter second number: "))  # Taking input and converting to integer
print("Sum of two numbers is: ", num1 + num2)  # Printing the sum

#also we can take input in one line like this
input("enter val:")
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
"WRITE A PROGRAM TO INPUT SIDE OF A SQUARE & PRINT ITS AREA"
side = int(input("Enter the side of square: "))  # Taking input and converting to integer
area = side * side  # Calculating area of square
print("Area of square is: ", area)  # Printing the area

#Value can be either int or float

side = float(input("Enter the value: ")) 
area = side * side
print("Area of square is: ", area)  # Printing the area
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
"WRITE A PROGRAM TO INPUT TWO FLOATING POINT NUMBERS & PRINT THEIR AVERAGE"
num1 = float(input("Enter first number: "))  # Taking input and converting to float
num2 = float(input("Enter second number: "))  # Taking input and converting to float
average = (num1 + num2) / 2  # Calculating average
#WE CALCULATE AVERAGE BY ADDING TWO NUMBERS AND DIVIDING BY 2 WITH [/]

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=a+b/2
print("Average is: ", c)  # Printing the average
#OR CAN BE WRITTEN AS
print("Average is: ", (a+b)/2)  # Printing the average

#------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
"WRITE A PROGRAM TO INPUT TWO INTEGER NUMBERS 'A' AND 'B'. PRINT TRUE IF 'A' IS GREATER THAN OR EQUAL TO 'B'. IF NOT PRINT FALSE"
A= int(input("Enter a: "))  # Taking input and converting to integer
B= int(input("Enter b: "))  # Taking input and converting to integer
C=A>=B
print(C)  
#OR WE CAN WRITE THIS PROGRAM AS INSTEAD OF WRITING C=A>=B
print(A>=B)
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------