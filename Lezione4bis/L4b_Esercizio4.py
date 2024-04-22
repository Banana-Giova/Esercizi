def majority_element(nums:int) -> int:
    """
        
        Data una lista nums di n elementi, restituire l'elemento che 
        compare più di n/2 volte.

        Esempio 1:
        nums = [3,2,3] -> restituire 3

        Esempio 2:
        nums = [2,2,1,1,1,2] -> restituire None

    """
    max_count = 0
    max_compar = 0          #inizializzo dei contatori, che di base sono pari a 0
    for i in nums:          #ciclo for per analizzare tutta la lista
        current_count = nums.count(i)       #contatore per l'iterazione corrente
        if current_count > max_count and current_count > max_compar:    #varia clausole
            max_count = current_count       #per verificare se il contatore attuale
            max_num = i     #eccede quello massimo e nel caso lo supera, aggiornare entrambi i contatori
            compar_error = False        #questo invece è una failsaife, che ora viene settata su False
        elif current_count == max_count and max_num != i:
            compar_error = True         #
            max_compar = current_count
        else:
            max_count = current_count
            max_num = i
            compar_error = False
            
    if compar_error == False and max_count > ((len(nums))/2):
        return max_num
    else:
        return None

if True:
    listonius = [3,3,3,2,4,4,1,3,3]
    print(majority_element(listonius))