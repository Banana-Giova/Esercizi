"""
10. Anagram Checker:

    Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not.
"""

def anagram_checker(first_str:str, second_str:str) -> str:
    punc = '''!’()-[]{};“”:'`"\\,<>./?@#$%^&*_~'''
    for i in first_str:
            if i in punc:
                first_str = first_str.replace(i, "")
    for i in second_str:
            if i in punc:
                second_str = second_str.replace(i, "")

    first_list:list[str] = list(first_str)
    second_list:list[str] = list(second_str)

    while " " in first_list:
        first_list.remove(" ")

    while " " in second_list:
        second_list.remove(" ")

    first_list = sorted(first_list)
    second_list = sorted(second_list)

    if first_list == second_list:
        return True
    else:
        return False
    

x:str = "the dogs were mad"
y:str = "methods wagered"

print(anagram_checker(x, y))