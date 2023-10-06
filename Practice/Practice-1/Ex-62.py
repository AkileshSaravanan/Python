'''
Scope in Python can be broadly categorized into two types: global scope and local scope

Global scope
Variables and functions defined outside of any function or class have global scope.
These entities can be accessed from anywhere in the code, both inside and outside functions or classes.
global_var = 10

def my_function():
    print(global_var)  # Accessing the global variable

print(global_var)  # Accessible here
my_function()  # Accessible here
Local scope
Variables defined within a function have local scope, meaning they are accessible only within that function.
Local scope is limited to the function where the variable is defined.
def my_function():
    local_var = 20  # Local variable
    print(local_var)  # Accessible here

print(local_var)  # Error: local_var is not defined (outside its scope)
Accessing Variables from Different Scopes
A function can access variables in its local scope, as well as variables in the global scope.
However, a local variable will take precedence over a global variable if they have the same name.
Review the code in the IDE and click on 'Submit' to know the result.
'''