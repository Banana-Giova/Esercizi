import os
import mmap
import PyPDF2 # type: ignore
import shutil

our_root = input("Inserisci la root directory >>> ")
if not os.path.isdir(our_root):
    print(f"Invalid directory! Current working directory: {os.curdir}\n")
    print(f"List of directories in the current working directory:\n{os.listdir()}\n")
    raise IsADirectoryError("This directory doesn't exist! The aforementioned directories are the one you can start choosing from!")
our_string = input("Inserisci la stringa da cercare >>> ")
our_outdir = input("Inserisci la directory di output >>> ")


#Metodo 1
def CercaStringaInFileName(input_file:str,input_string:str):
    curr_file = input_file.casefold()
    curr_string = input_string.casefold()
    print(f"Cerco {input_file} in {input_string}")

    flag = curr_file.find(curr_string)
    if flag > -1:
        print("Trovato")
        return True
    return False


#Metodo 2
def CercaInFilePdf(input_path,input_string:str):
    curr_string = input_string.casefold()
    pdfile = PyPDF2.PdfFileReader(input_path)
    numPages = len(pdfile.pages)

    for i in range(0, numPages):
        single_page = pdfile.pages[i]
        text = single_page.extract_text()
        text = text.casefold()
        if text.find(curr_string) != -1:
            return True

    return False


#Metodo 3
def CercaInTextFile(input_path,input_string:str):
    content = -1
    with open(input_path) as curr_file:
        single_line = curr_file.readline()
        while len(single_line) > 0:
            content = single_line.casefold().find(input_string.casefold())
            if content >= 0:
                return True
            single_line = curr_file.readline()

    return False


#Metodo 4
def CercaStringaInFileContent(input_path:str,input_string:str):
    curr_string = input_string.casefold()

    if input_path.endswith(".pdf"):
        print("Rilevato file PDF.")
        return CercaInFilePdf(input_path=input_path, 
                              input_string=input_string)

    if input_path.endswith(".txt"):
        print("Rilevato file TXT.")
        return CercaInTextFile(input_path=input_path, 
                              input_string=input_string)

    try:
        with open(input_path) as path:
            file_content = mmap.mmap(path.fileno(), 0, access=mmap.ACCESS_READ)
            mmap_output = file_content.readline()
            while len(mmap_output) > 0:
                mmap_output.casefold()
                if mmap_output.find(curr_string.encode()) != -1:
                    return True
                else:
                    mmap_output = file_content.readline()
    except:
        return False


#Metodo 5
def SalvaFile(curr_path, curr_filename, curr_outdir):
    os.makedirs(curr_outdir, exist_ok=True)
    new_file = curr_outdir + "/" + curr_filename
    while True:
        copycat:str = "(copy)"
        copycount:str = ""
        if os.path.exists(new_file):
            copycount += copycat
            newer_file = os.path.splitext(new_file)
            new_file = newer_file[0] + copycount + newer_file[1]
        else:
            break

    shutil.copyfile(curr_path, new_file)


#Execution
match_counter = 0
for root, dirs, files in os.walk(our_root):
    print(f"Directory corrente {0} contenente {1} subdir e {2} files")
    for filename in files:
        name_searcher = CercaStringaInFileName(filename,our_string)
        if name_searcher:
            print(f"Trovato file: {filename}")
            match_counter += 1
            SalvaFile(root, filename, our_outdir)
        else:
            full_path = os.path.join(root, filename)
            content_searcher = CercaStringaInFileContent(full_path, our_string)
            if content_searcher:
                print(f"Trovato: {filename}")
                match_counter += 1
                SalvaFile(root, filename, our_outdir)

