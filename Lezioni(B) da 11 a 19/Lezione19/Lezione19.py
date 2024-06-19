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
                if fi == len(first_half):
                    return new_listing + second_half[si:]
            else:
                new_listing.append(second_half[si])
                si += 1
                if si == len(second_half):
                    return new_listing + first_half[fi:]
    else:
        return listing
    
def merge(list_1: list[int], list_2: list[int]) -> list[int]:
    
    i, j = 0, 0
    
    result: list[int] = [None for _ in range(len(list_1 + list_2))]
    
    for k in range(len(result)):
        
        if list_1[i] > list_2[j]:
            
            result[k] = list_2[j]
            j += 1
            
            if j == len(list_2):
                
                return result[:k+1] + list_1[i:]
            
        else:
            
            result[k] = list_1[i]
            i += 1
            
            if i == len(list_1):
                
                
                return result[:k+1] + list_2[j:]


def bubble_sort_v2(x: list[int]):
    # Ω(n) -> caso migliore quando la lista è già ordinata
    # O(n^2) -> caso peggiore
    ho_fatto_swap: bool = True
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                # swap(x[j], x[j+1])
                ho_fatto_swap = False
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if ho_fatto_swap:
            break


if __name__ == "__main__":
    
    import random
    import time
    import matplotlib.pyplot as plt
    
    merge_sort_times: list[float] = []
    bubble_sort_times: list[float] = []
    cases = [10, 50, 100, 250, 500, 1000, 1500, 2000, 5000, 10000, 20000]
    for n in cases:
        
        list_input: list[int] = [random.randint(0, 100000) for _ in range(n)]
        
        start = time.time()    
        result: list[int] = mergeSort(listing=list_input)
        end = time.time()
        
        merge_sort_times.append(end-start)
            
        start = time.time()
        result: list[int] = bubble_sort_v2(x=list_input)
        end = time.time()
        
        bubble_sort_times.append(end-start)
        
    print(f"MERGE: {merge_sort_times}\nBUBBLE: {bubble_sort_times}")
    plt.plot(cases, merge_sort_times, label="Merge")
    plt.plot(cases, bubble_sort_times, label="Bubble")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.show()