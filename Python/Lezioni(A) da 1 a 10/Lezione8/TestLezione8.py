#Esercizio 1

def longest_palindrome(s: str) -> int:
    output = 1
    s_to_list:list[str] = list(s)
    if reversed(s_to_list) == s_to_list:
        return len(s_to_list)
    else:
        palindict:dict[int, str] = {}
        for i in s_to_list:
            if i not in palindict:
                palindict[i] = s_to_list.count(i)
        
        all_good:bool = True
        for ki, vi in palindict.items():
            if vi%2 == 0:
                output += vi
            elif vi == 1:
                all_good = False
            else:
                all_good = False
                if (vi-1)%2 == 0\
                and vi-1 > 0:
                    output += vi-1


    if all_good == True:
        output -= 1

    return output

#Esercizio 2

def merge(nums1:list[int], m, nums2:list[int], n):
    while True:
        if nums1[-1] == 0\
        and len(nums1) != 1\
        and len(nums1) > m:
            nums1.pop(-1)
        elif len(nums1) == 1\
        and nums1[0] == 0:
            nums1.clear()
            break
        else:
            break

    nums1 += nums2
    nums1.sort()
    
    return nums1 

#Esercizio 3

class MyStack:

    def __init__(self):
        self.stack:list = []

    def push(self, x: int) -> None:
        if x not in self.stack:
            self.stack.append(x)
        else:
            self.stack.remove(x)
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) != 0:
            temptopo = self.stack.pop(-1)

        return temptopo

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
        
#Esercizio 4

class LinkedList:
    def __init__(self, head=0, next=None):
        self.head = head
        self.next = next
    
    def getNext(self):
        return self.next
    
    def setNext(self,newnext):
        self.next = newnext
    
    def append(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(LinkedList(item))
        else:
            self.head = LinkedList(item)
        
def is_palindrome(head) -> list[int]:
    glorb:list = []
    while head:
        glorb.append(head.head)
        head = head.next

    glarb:list = []
    for i in reversed(glorb):
        glarb.append(i)
    if glorb == glarb:
        return True
    else:
        return False
    
#Esercizio 5

def is_valid_parenthesis(s: str) -> bool:
    s_to_list:list[str] = list(s)
    round_opened:bool = False
    squared_opened:bool = False
    curly_opened:bool = False
    invalid:bool = False
    last_opened:None = None
    pen_last_opened:None = None

    if s_to_list.count("(") != s_to_list.count(")")\
    or s_to_list.count("[") != s_to_list.count("]"):
        return False
    
    for i in s_to_list:
        if i == "(":
            round_opened = True
            if last_opened == None:
                last_opened = i
            else:
                pen_last_opened = i
        elif i == ")" and round_opened == True:
            round_opened = False
        elif i == "[":
            squared_opened = True
            if last_opened == None:
                last_opened = i
            else:
                pen_last_opened = i
        elif i == "]" and squared_opened == True:
            squared_opened = False
        elif i == "{":
            curly_opened = True
            if last_opened == None:
                last_opened = i
            else:
                pen_last_opened = i
        elif i == "}" and curly_opened == True:
            curly_opened = False

    for i in range(len(s_to_list)-1):
        if s_to_list[i] == "(":
            if s_to_list[i+1] == "]" or s_to_list[i+1] == "}":
                invalid = True
        elif s_to_list[i] == "[":
            if s_to_list[i+1] == ")" or s_to_list[i+1] == "}":
                invalid = True
        elif s_to_list[i] == "{":
            if s_to_list[i+1] == ")" or s_to_list[i+1] == "]":
                invalid = True

    if round_opened == False\
    and squared_opened == False\
    and curly_opened == False\
    and invalid == False:
        return True
    else:
        return False