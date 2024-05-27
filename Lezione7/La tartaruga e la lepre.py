import random

percorso:list[int] = ["_" for i in range(1, 71)]
tartaruga:int = 0
tartamina:int = 100
lepre:int = 0
leprergia:int = 100

modifiers:dict[int, tuple[int, str]] = {10: (5, "BONUS"),
                                        15: (-3, "MALUS"),
                                        25: (3, "BONUS"),
                                        30: (-5, "MALUS"),
                                        45: (-7, "MALUS"),
                                        50: (10, "BONUS")}

def view_pos(tartaruga:int, lepre:int) -> str:
    print(f"THE TURTLE IS IN THE SQUARE N. {tartaruga+1}!\n"\
        + f"THE HARE IS IN THE SQUARE N. {lepre+1}!")
    
def tarta_choice(tartaruga:int, tartamina:int) -> str:
    tired:bool = False
    tarta_movement:dict[int, int] = {1: (3, 5),
                                     2: (3, 5),
                                     3: (3, 5),
                                     4: (3, 5),
                                     5: (3, 5),
                                     6: (-6, 10),
                                     7: (-6, 10),
                                     8: (1, 3),
                                     9: (1, 3),
                                    10: (1, 3)}
    
    choice = random.randint(1, 10)
    tartamina -= tarta_movement[choice][1]
    if tartamina <= 0:
        tartamina = 0
        tired = True
        print("THE TORTOISE IS TIRED!!!")

    if tired != True:
        tartaruga += tarta_movement[choice][0]

    if tartaruga < 0:
        tartaruga = 0
    return tartaruga

def lep_choice(lepre:int, leprergia:int) -> str:
    tired:bool = False
    lep_movement:dict[int, int] = {1: (0, -5),
                                   2: (0, -5),
                                   3: (9, 15),
                                   4: (9, 15),
                                   5: (-12, 20),
                                   6: (1, 5),
                                   7: (1, 5),
                                   8: (1, 5),
                                   9: (-2, 8),
                                  10: (-2, 8)}
    
    choice = random.randint(1, 10)
    leprergia -= lep_movement[choice][1]
    if leprergia <= 0:
        leprergia = 0
        tired = True
        print("THE HARE IS TIRED!!!")

    if tired != True:
        lepre += lep_movement[choice][0]

    if lepre < 0:
        lepre = 0
    return lepre



winner:bool = False
weather:int = 0
pioggia:bool = 0

print("BANG !!!!! AND THEY'RE OFF !!!!!")
while winner == False:
    percorso:list[int] = ["_" for i in range(1, 71)]
    weather += 1
    if weather > 9:
        weather = 0
        pioggia:bool = random.getrandbits(1)

    tartaruga = tarta_choice(tartaruga, tartamina)
    lepre = lep_choice(lepre, leprergia)

    if (tartaruga+1) in modifiers:
        print(f"THE TORTOISE STEPPED ON A {modifiers[tartaruga+1][1]}!!!")
        tartaruga += modifiers[tartaruga+1][0]
    if (lepre+1) in modifiers:
        print(f"THE HARE STEPPED ON A {modifiers[lepre+1][1]}!!!")
        lepre += modifiers[lepre+1][0]
        

    if pioggia == True:
        print("IT'S RAINING!!!")
        if tartaruga > 1:
            tartaruga -= 1
        if lepre > 2:
            lepre -= 2
    else:
        print("THE SUN SHINES!!!")

    if tartaruga > 69 and lepre > 69\
    and tartaruga == lepre:
        winner = True
        print("IT'S A TIE")
    elif tartaruga > 69:
        winner = True
        print("TORTOISE WINS! || VAY!!!")
        continue
    elif lepre > 69:
        winner = True
        print("HARE WINS || YUCH!!!")
        continue

    if tartaruga == lepre:
        percorso[lepre] = "OUCH!!!"
    else:
        percorso[tartaruga] = "T"
        percorso[lepre] = "H"

    tartamina += 10
    if tartamina > 100:
        tartamina = 100
    leprergia += 10
    if leprergia > 100:
        leprergia = 100

    print(percorso)
    view_pos(tartaruga, lepre)