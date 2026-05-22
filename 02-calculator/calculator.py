"""
Calculator Functions Module

This module contains the basic arithmetic operations.
Each function takes two numbers and returns the result.

Concepts demonstrated:
- Function definition
- Parameters and return values
- Docstrings (documentation)
- Error handling
"""


def add(a, b):
    """
    Add two numbers
    
    Parameters:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    
    Example:
        >>> add(5, 3)
        8
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers
    
    Parameters:
        a (float): First number
        b (float): Second number (to subtract)
    
    Returns:
        float: Difference (a - b)
    
    Example:
        >>> subtract(10, 3)
        7
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers
    
    Parameters:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    
    Example:
        >>> multiply(4, 5)
        20
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers
    
    Parameters:
        a (float): Numerator (dividend)
        b (float): Denominator (divisor)
    
    Returns:
        float: Quotient (a / b)
    
    Raises:
        ZeroDivisionError: If b is zero
    
    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
