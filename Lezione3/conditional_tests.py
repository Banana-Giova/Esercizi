"""
5-2. More Conditional Tests: 
You don’t have to limit the number of tests you create to 10. 
If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

if True:
    #5-2. More Conditional Tests:
    cat:str = "Peppino"
    floppa:str = "Caracal"
    car:str = "Smart"
    lucky:int = 47
    dead_lucky:int = 4774
    animals:list[str] = ["Cat", "Caracal", "Cheetah", "Cougar", "Leopard", "Lion", "Lynx", "Puma", "Tiger"]

    print("Is cat == car? I predict False.")
    print(cat == car)
    print("\nIs cat == cat, but in lowercase? I predict False.")
    print(cat == cat.lower())
    print("\nIs 4774 >= 47? I predict True.")
    print(dead_lucky >= lucky)
    print("\nIs cat == car and 47 > 4774? I predict False.")
    print(cat == car and lucky > dead_lucky)
    print("\nIs cat != car or 47 > 4774? I predict True.")
    print(cat != car or lucky > dead_lucky)
    print("\nIs cat in animals? I predict False.")
    print(cat in animals)
    print("\nIs floppa in animals? I predict True.")
    print(floppa in animals)