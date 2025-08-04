print("it's kulvir here")   # where print is function 
 
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
 
