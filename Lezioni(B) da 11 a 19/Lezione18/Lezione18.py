"""
Esercizio 1

An interactive calculator: 
- It is required to develop an interactive calculator 
with at least 10 test cases using UnitTest (possibly) all execution paths!
User input is assumed to be a formula that consists of a number, 
an operator (at least + and -), and another number, 
separated by white space (e.g. 1 + 1). Split user input using str.split(), 
and check whether the resulting list is valid:

    - If the input does not consist of 3 elements, raise a FormulaError, 
      which is a custom Exception.
    - Try to convert the first and third inputs to a float 
      (like so: float_value = float(str_value)). 
    - Catch any ValueError that occurs, and instead raise a FormulaError.
    - If the second input is not '+' or '-', again raise a FormulaError.
    - If the input is valid, perform the calculation and print out the result. 
      The user is then prompted to provide new input, 
      and so on, until the user enters quit.
"""
class FormulaError(Exception):
    """Invalid formula."""

def calculon():
    print("Input a string contaning numbers and operators."\
          "Be consistent with white spaces.\nTo quit enter 'quit'.\n")
    while True:
        user_input:str = input(">>> ")
        if user_input == "quit":
            break

        if " " in user_input:
            elements:list[str] = user_input.split()
            if "+" not in elements and "-" not in elements:
                raise FormulaError
            else:
                operator:str = elements[1]
        else:
            if "+" in user_input:
                elements:list[str] = user_input.split("+")
                operator:str = "+"
            elif "-" in user_input:
                elements:list[str] = user_input.split("-")
                operator:str = "-"
            else:
                raise FormulaError
        
        try:
            first_num:float = float(elements[0])
        except ValueError:
            raise FormulaError
        try:
            second_num:float = float(elements[-1])
        except ValueError:
            raise FormulaError
        
        if operator == "+":
            output:float = first_num + second_num
        elif operator == "-":
            output:float = first_num - second_num
        else:
            raise FormulaError
        
        print(output)

"""
Esercizio 2

Personalized math library: 
-Create a Python library that provides functions for handling fractions, 
with built-in error handling. The library must include functions 
for the following operations:

    - Create a fraction from the numerator and denominator.

    - Collect the numerator and denominator of a fraction.

    - Simplify a fraction.

    - Add, subtract, multiply and divide fractions.

    - Check whether one fraction is equivalent to another.

    - All library functions must use the try-except block to handle potential errors, 
      such as null denominators, unsupported operations, or division by zero. 
      The library must raise custom exceptions to indicate specific errors to the user.
"""
class FractionError(Exception):
    """Invalid fraction."""
class InputError(Exception):
    """Invalid inputs."""

class FractionHandling:
    
    @staticmethod
    def createFraction(numerator:int, denominator:int) -> str:
        if denominator == 0:
            raise ZeroDivisionError
        try:
            return f"{numerator}/{denominator}"
        except Exception:
            raise InputError
    
    @staticmethod
    def dismantleFraction(fraction:str) -> list[int, int]:
        try:
            output:list = fraction.split("/")
            for i in output:
                int(i)
            return output
        except Exception:
            raise FractionError
        
    @staticmethod
    def simplifyFraction(fraction:str) -> str:
        pass

    @staticmethod
    def operationFraction(fraction1:str, fraction2:str) -> str:
        pass

    @staticmethod
    def equivalentFraction(fraction1:str, fraction2:str) -> str:
        pass