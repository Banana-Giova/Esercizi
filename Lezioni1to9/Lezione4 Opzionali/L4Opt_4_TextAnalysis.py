"""
4. Text Analysis:

    Create a function that reads a text file and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
    Implement error handling to handle missing files or other input issues.
"""

f = open('Lezione4/Lezione4_Opzionali/data/alice.txt', 'r')
content = f.read()
f.close()

def text_analysis(text_to_check:str) -> str:
    punc = '''!’()-[]{};“”:'`"\\,<>./?@#$%^&*_~'''
    word_occurences:dict = {   
    }
    common_words:list[int] = [i + 1 for i in range(0, 1000)]
    low_alphabet:list = list(map(chr, range(ord('a'), ord('z')+1)))
    upp_alphabet:list = []
    for i in low_alphabet:
        upp_alphabet.append(i.capitalize())
    common_words.extend(low_alphabet)
    common_words.extend(upp_alphabet)
    common_words.append('\n')
    common_words.append('\n\n')
    common_words.append('')

    try:
        for i in text_to_check:
            if i in punc:
                text_to_check = text_to_check.replace(i, " ")
        listext:list[str] = text_to_check.split(" ")

        for i in listext:
            if i not in word_occurences and i not in common_words:
                current_count:int = text_to_check.count(i)
                if current_count not in common_words and i not in common_words:
                    word_occurences[i] = current_count
    except Exception:
        print("Error, invalid text given or missing files.")
                    

    print(word_occurences)
    
text_analysis(content)