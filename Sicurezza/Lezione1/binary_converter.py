def to_binary(file_in:str, file_out:str):
    print("Inizio conversione in binario del file...")
    try:
        with open(file_in, mode='rb') as f:
            data = f.read()
        with open(file_out, mode='w') as f:
            for i in data:
                f.write(str(i))
                f.write("\n")
    except Exception as e:
        raise RuntimeError(e)
    print("File convertito in binario con successo.")

def from_binary(file_in:str, file_out:str):
    print("Inizio conversione dal binario del file...")
    try:
        with open(file_in, mode="r") as fin:
            with open(file_out, mode="wb") as fou:
                nums = fin.readlines()
        for num in nums:
            a = int(num).to_bytes()
            fou.write(a)
    except Exception as e:
        raise RuntimeError(e)
    print("File convertito in binario con successo.")

fin:str = str(input("Inserire file da convertire.\n>>>"))
fout:str = str(input("Inserire file di output.\n>>>"))
mode:str = str(input("Digitare 'TB' se si desidera convertire in binario o 'FB' se si desidera convertire dal binario.\n>>>"))
if mode == 'TB':
    to_binary(fin,fout)
elif mode == 'FB':
    from_binary(fin,fout)
else:
    print("Modalità selezionata invalida.")