def move_zeroes(nums:list[int]):
    """
        Data una lista nums di interi, spostare gli zeri alla fine 
        di questa lista mantenendo l'ordine originale dei numeri che
        non sono zeri.

        Esempio 1:
        nums = [0,1,0,3.12] -> modificare la lista in [1,3,12,0,0]

        Esempio 2:
        nums = [0] -> la modifica è nulla perché abbiamo uno zero
        che non si sposta


    """

    zeraora:list[int] = []
    for i in nums:
        if i == 0:
            zeraora.append(0)
        else:
            continue
    for i in zeraora:
        nums.remove(0)
    nums.extend(zeraora)

    return nums

print(move_zeroes([3,2,0,0,4,0,5,0,2,2]))