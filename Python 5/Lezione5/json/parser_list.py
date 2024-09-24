def Deserializza(serialized_str:str) -> list:
    blacklist:list = ['\'', '"', '[', ']', ',']
    output_list:list[str] = []
    new_word:str = ""
    for i in serialized_str:
        if i not in blacklist:
            new_word += i
        else:
            if new_word != "" and new_word != " ":
                output_list.append(new_word)
            new_word = ""
    return output_list

def SerializzaLista(deserialized_list:list) -> str:
    return str(deserialized_list)


mylist_1:str = "['mario', 'gino', 'lucrezia']"
mylist_2:list = ['mario', 'gino', 'lucrezia']

print(Deserializza(mylist_1))
print(SerializzaLista(mylist_2))
print(Deserializza(mylist_1) == mylist_2)
print(SerializzaLista(mylist_2) == mylist_1)