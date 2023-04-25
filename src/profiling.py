import sys
import re
import math_lib
from math_lib import MathLib
# Define variables
sum_of_squares = 0.0      # sum of squares of all numbers
sum_of_numbers = 0.0      # sum of all numbers
num_in_pow = 0.0          # number in power of 2
not_num = 0.0             # 'not number in power of 2
quantity = 0              # quantity of numbers
result = 0.0              # Final result
prvni_slozka = 0.0        #prvni_slozka=1/(N-1)
druha_slozka = 0.0        #druha_slozka=suma(x^2)-N*(not_num)^2


if len(sys.argv) < 2:
        print('Usage: \n'
            'python profiling.py "filename"\n'
            'python profiling.py "number1 number2 number3..."')
        sys.exit()

if len(sys.argv) == 2:
        filename = sys.argv[1] 

        # Open file and read data
        with open(filename, 'r') as array:
            for elements in array:
                if not elements.strip(): # skip empty lines
                    continue
                
                data = re.split('[\t\s]+', elements.strip())
                for number in data:
                    sum_of_numbers=MathLib.add(sum_of_numbers, float(number)) #sum of all numbers
                    num_in_pow=MathLib.pow(float(number), 2) #number in power of 2
                    sum_of_squares=MathLib.add(sum_of_squares, num_in_pow) #sum of squares of all numbers
                    quantity=MathLib.add(quantity, 1) #quantity of numbers
            not_num=MathLib.mul(sum_of_numbers, MathLib.div(1, quantity))
            prvni_slozka=MathLib.div(1, MathLib.sub(quantity, 1))
            druha_slozka=MathLib.sub(sum_of_squares, MathLib.mul(quantity, MathLib.pow(not_num, 2)))

            result=MathLib.root(MathLib.mul(prvni_slozka, druha_slozka), 2)
            print(result)

if len(sys.argv) > 2:
        input_array = sys.argv[1:] # read data from command line arguments from 2nd argument
        for elements in input_array:
            data = re.split('[\t\s]+', elements.strip())
            for number in data:
                sum_of_numbers=MathLib.add(sum_of_numbers, float(number)) #sum of all numbers
                num_in_pow=MathLib.pow(float(number), 2) #number in power of 2
                sum_of_squares=MathLib.add(sum_of_squares, num_in_pow) #sum of squares of all numbers
                quantity=MathLib.add(quantity, 1) #quantity of numbers

        not_num=MathLib.mul(sum_of_numbers, MathLib.div(1, quantity))
        prvni_slozka=MathLib.div(1, MathLib.sub(quantity, 1))
        druha_slozka=MathLib.sub(sum_of_squares, MathLib.mul(quantity, MathLib.pow(not_num, 2)))

        result=MathLib.root(MathLib.mul(prvni_slozka, druha_slozka), 2)
        print(result)