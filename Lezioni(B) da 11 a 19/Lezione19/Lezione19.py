def mergeSort(listing:list[int] | list[float]) -> list:

    midpoint:int = len(listing)//2

    if len(listing) > 1:
        first_half = mergeSort(listing=listing[:midpoint])
        second_half = mergeSort(listing=listing[midpoint:])
        new_listing = []
        fi, si = 0, 0
        for i in range(len(first_half + second_half)):
            if first_half[fi] < second_half[si]:
                new_listing.append(first_half[fi])
                fi += 1
                if fi > (len(first_half)-1):
                    new_listing.append(second_half[si])
            else:
                new_listing.append(second_half[si])
                si += 1
                if si > (len(second_half)-1):
                    new_listing.append(first_half[fi])
    else:
        return listing
    
mergeSort([3,2,4,5,2,1])