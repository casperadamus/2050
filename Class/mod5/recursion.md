Recursion:

A recursion function is just like any other function, but this time it calls itself. 

Structure:

```python
def recurseive_function(parameters):
  if base_case_condition:
    return base_case_value
  else:
    recursive_function(modified_parameters)
```

Recursive function contains two key parts:

Base Case - The stopping condition that prevents infinite recursion.

Recursive Case - The part of the function where it calls itself with modified parameters. 


Example 1: Factorial Calculation

```python
def factorial(n):
  if n == 0: # Base Case
    return 1
  else:       # Recursive Case
    return n * factorial(n-1) 

print(factorial(5)) # Output: 120
```


Base Case: When n == 0, recursion stops and returns 1. 

Recursive Case: Multiplies n by the result of factorial(n-1), which continues to call itself until it reaches the base case.

 
