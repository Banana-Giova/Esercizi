def float_inputter() -> float:
    """
        This function allows the user to input a float easily, 
        without incurring in errors if the number is not valid.
    """
    inputted_number = ""
    while True:
        
        inputted_number = input("Input a number -> ")
        try:
            float(inputted_number)
            break
        except ValueError:
            print("Error, input a valid number.")
            inputted_number = ""
            continue
    return float(inputted_number)

def int_inputter() -> int:
    """
        This function allows the user to input an int easily, 
        without incurring in errors if the number is not valid.
    """
    inputted_number = ""
    while True:
        
        inputted_number = input("Input a number -> ")
        try:
            int(inputted_number)
            break
        except ValueError:
            print("Error, input a valid number.")
            inputted_number = ""
            continue
    return int(inputted_number)

if False:
    #(Y/n) Manager
    while True:
        choice:str = (input("Choice Placeholder?(Y/n)")).lower()
        if choice == "y":
            #Y choice placeholder
            break
        elif choice == "n":
            #n choice placeholder
            break
        else:
            print("Invalid choice, type 'Y' or 'n'.")