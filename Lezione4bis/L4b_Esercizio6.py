def intersection(nums1:list[int], nums2: list[int]) -> list[int]:
    """
        Restituisce i numeri in comune fra due liste.
    """

    list_set:list = []      #creo una lista vuota che conterrà gli elementi in comune
    for i in nums1:
        if i in nums2:      #ciclo for per iterare ed inserire i numeri in comune
            list_set.append(i)
        else:
            continue

    return set(list_set)

print(intersection([2,2,4,2,1], [1,1,2,0,2,1,2]))