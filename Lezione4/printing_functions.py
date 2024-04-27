"""
8-15. Printing Models: 
- Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
8-16. Imports: 
- Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
8-17. Styling Functions: 
- Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
"""

from Lezione4 import make_car

if True:
    #8-15. Printing Models:

    make_car("Subaru", "Outback", Color = "Blue", Tow_Package = True)