def third_max(nums: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    # potete utilizzare queste tre variabili di comodo
    first_max = second_max = third_max = None
    if len(nums) > 2:
        print("Exit1")
        for i in nums:
            print(i)
            if first_max == None:
                first_max = i
            elif second_max == None and i != first_max:
                second_max = i
            elif third_max == None and i != first_max and i != second_max:
                third_max = i
            else:
                continue
        if third_max == None:
            third_max = 0
            for i in nums:
                if i > third_max:
                    third_max = i
                else:
                    continue
            return third_max
        else:
            return third_max


    else:
        print("Exit2")
        third_max = 0
        for i in nums:
            if i > third_max:
                third_max = i
            else:
                continue
        return third_max
    
def blackjack_hand_total(cards: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    blackjack_hand_total:int = 0
    ace:int = 0
    for i in cards:
        if i == 11:
            ace += 1
        else:
            blackjack_hand_total += i
    while ace > 0:
        if (blackjack_hand_total + 11) > 21:
            blackjack_hand_total += 1
            ace -= 1
        else:
            blackjack_hand_total += 11
            ace -= 1
    return blackjack_hand_total

def even_odd_pattern(nums: list[int]) -> list[int]:
    # cancella il pass e inserisci il tuo codice
    nums_even:list = []
    nums_copy = nums.copy()
    for i in nums_copy:
        if i % 2 != 0:
            nums_even.append(i)
            nums.remove(i)
        else:
            continue
    nums.extend(nums_even)
    return nums

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    # elimina il pass e inserisci il codice
    disappeared_numbers:list = []
    alpaca:list = []
    for i in range(1, (len(nums) +1)):
        alpaca.append(i)

    for i in alpaca:
        if i not in nums:
            disappeared_numbers.append(i)
        else:
            continue
    return disappeared_numbers

def prime_factors(n: int) -> list[int]:
    # elimina il pass e implementa la tua soluzione
    n = abs(n)
    prime_factors:list = []
    while (n % 2) == 0:
        prime_factors.append(2)
        n /= 2
    i = 3
    while i * i <= n:
        if n % i != 0:
            i += 1
        else: 
            n /= i
            n = int(n)
            prime_factors.append(i)
    
    if n > 1:
        prime_factors.append(int(n))

    return prime_factors

print(prime_factors(99999999999999999999))