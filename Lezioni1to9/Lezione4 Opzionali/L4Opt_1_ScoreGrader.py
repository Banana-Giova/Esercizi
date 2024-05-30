"""
1. School Grading System:

    Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, 
    and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
"""

def score_grader(name:str, score:list[int]) -> str:
    
    grade:float = sum(score)/len(score)
    if grade >= 60:
        return f"""{name} your average is {grade}, 
        which means that you passed the exam! Congratulations!"""
    else:
        return f"""{name} your average is {grade}, 
        which means that you failed the exam! :("""
    
students:dict[str, list[int]] = {"Peppino": [40, 55, 70, 85], 
                                    "Ciro": [20, 40, 60, 80], 
                                    "Mimmo": [22, 27, 34, 37],
                                    "Pedro": [57, 69, 77, 88],
                                    "Rachele": [92, 96, 100, 99],
                                    "Sandro": [79, 51, 45, 72],
                                    "Elia": [24, 56, 74, 67],
                                    "Romeo": [89, 78, 67, 98]}

for ki, vi in students.items():
    print(score_grader(ki, vi))