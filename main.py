# Lambda

# Step 1

# In this project, you're going to build a simple, yet functional expense tracker in Python.

# Start by defining a function named add_expense that takes three parameters: 
# expenses, amount and category. Use the pass keyword to fill the function body.

def add_expense(expenses, amount, category):
    pass

# Step 2

# A list in Python is a built-in data type that allows you to store many items in a single data structure. 
# In Python, you create a list by putting items inside square brackets [], 
# with each item separated from the following one by a comma.

numbers = [1, 2, 3, 4]

# Create an empty list named expenses. You will use it to store each of your expenses.

expenses = []

# Step 3

# The expenses parameter of your add_expense function will be a list of expenses. 
# You want to be able to add items at the end of your list. For that you can use the .append() list method:

my_list = [2, 4, 7]
my_list.append(3)

#In the example above, after appending 3, my_list would be [2, 4, 7, 3]. 
# Replace pass with a call to the .append() method on the expenses list. 
# Don't pass any arguments to .append() for now.

def add_expense(expenses, amount, category):
    expenses.append()

# Step 4

# A dictionary is another built-in data type in Python. 
# A dictionary is a collection of data in the form of key-value pairs. 
# Dictionaries are defined with curly braces {} and they contain key-value pairs separated by commas. 
# Each key is followed by a colon : and the value:

{"amount": 50.0, "category": "Food"}

# In the example above, amount and category are keys, and 50.0 and Food are their the corresponding values.

# Create a dictionary with a key amount and value of the amount parameter and pass your new dictionary to the .append() call.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount})

# Step 5

# Add another key-value pair to the dictionary you are appending to the expense list. 
# Use the string category as the key, and the category parameter as the value.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Step 6

# Start by defining a function named print_expenses that takes one parameter expenses. 
# This function will later be used to display each expense in your list.

# Fill the body of your new function with a pass statement.

def print_expenses(expenses):
    pass

# Step 7

# Inside the print_expenses function, create a for loop that iterates over each item in the expenses list. 
# Use expense as the loop variable and move pass inside the loop body.

def print_expenses(expenses):
    for expense in expenses:
        pass

# Step 8

# Next, you are going to display the details for each expense.

# Inside the for loop, replace pass with a print() call and pass it the following 
# f-string: f'Amount: {expense}, Category: {expense}'. 
# Leave the placeholders empty for now.

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense}, Category: {expense}')

# Step 9

# You can access values in a dictionary through its keys. 
# You need to use the bracket notation and include the key between the square brackets:

my_dict = {"amount": 50.0, "category": "Food"}
my_dict["amount"] # 50.0

# You are currently interpolating the expense dictionary in your f-string. 
# Modify the f-string expression to access the value of the amount key and the category key 
# in the expense dictionary.

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


