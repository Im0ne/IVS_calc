## @file math_lib.py
# @brief Math library for the project
# 
# 

## @class MathLib
# @brief Math operations

class MathLib(object):
    
        ## @brief Addition
        # @return The sum of a and b
        def add(a, b):
            return a + b
    
        ## @brief Subtraction
        # @return The difference of a and b
        def sub(a, b):
            return a - b
    
        ## @brief Multiplication
        # @return The product of a and b
        def mul(a, b):
            return a * b
    
        ## @brief Division
        # @return The quotient of a and b
        def div(a, b):
            return a / b
    
        ## @brief Power
        # @return The power of a and b
        def pow(a, b):
            return a ** b
    
        ## @brief Square root
        # @return  The root in b of a
        def root(a, b):
            return a ** (1 / b)
    
        ## @brief Factorial
        # @return The factorial of a
        def fact(a):
            if a < 0:
                return -1
            elif a == 0:
                return 1
            else:
                for i in range(1, a):
                    a *= i
                return a
            
    
        ## @brief Absolute value
        # @return The absolute value of a
        def abs(a):
            if a < 0:
                return -a
            else:
                return a
    
       
