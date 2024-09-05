import time

def decorator(func):

    def wrapper(*args):
        import time

        start = time.time()

        func(*args)

        print(f"{time.time() - start}\n")

    return wrapper

class Timer:
    def __enter__(self, average:int):
        self.time = time.time()
        self.average = average

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.time() - self.time
        print(f"{self.elapsed/self.average}")
        print(f"Total time elapsed: {self.elapsed}")

class ContextManagerOnRead:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def __enter__(self):
        self.file_obj = open(self.file_path, mode='r')
        return self.file_obj

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_obj:
            self.file_obj.close()
        else:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")

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
    #print(word_occurences)



print("Program started. It can take up to 4 minutes.\nPatience is a virtue!\n\n")

#Manual open() and close()
print('\nAverage time elapsed with manual "open()" and "close()":')
with Timer(30):
    f = open('data/alice.txt', 'r')
    content = f.read()
    f.close()
    for i in range(30):
        text_analysis(content)


#with statement
print('\nAverage time elapsed with a "with" statement:')
with Timer(30):
    with open('data/alice.txt', 'r') as reader:
        content = reader.read()
        for i in range(30):
            text_analysis(content)


#ContextManager
print('\nAverage time elapsed with a Context Manager:')
with Timer(30):
    with ContextManagerOnRead('data/alice.txt') as reader:
        content = reader.read()
        for i in range(30):
            text_analysis(content)