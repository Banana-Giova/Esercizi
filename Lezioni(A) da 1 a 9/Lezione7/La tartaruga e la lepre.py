import random
import copy

percorso:list[str] = ["_" for i in range(1, 71)]
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
    tarta_movement:dict[int, tuple[int, int]] = {1: (3, 5),
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
    if tartamina < tarta_movement[choice][1]:
        print("THE TORTOISE IS TIRED!!!")
        tarta_tired:bool = True
        tartamina += 10
    else:
        tartaruga += tarta_movement[choice][0]
        tartamina -= tarta_movement[choice][1]
        tarta_tired:bool = False

    if tartaruga < 0:
        tartaruga = 0
    return tartaruga, tartamina, tarta_tired

def lep_choice(lepre:int, leprergia:int) -> str:
    lep_movement:dict[int, tuple[int, int]] = {1: (0, -10),
                                               2: (0, -10),
                                               3: (9, 15),
                                               4: (9, 15),
                                               5: (-12, 20),
                                               6: (1, 5),
                                               7: (1, 5),
                                               8: (1, 5),
                                               9: (-2, 8),
                                              10: (-2, 8)}
    
    choice = random.randint(1, 10)
    if leprergia < lep_movement[choice][1]:
        print("THE HARE IS TIRED!!!")
        lep_tired:bool = True
    else:
        lepre += lep_movement[choice][0]
        leprergia -= lep_movement[choice][1]
        lep_tired:bool = False

    if leprergia > 100:
        leprergia = 100

    if lepre < 0:
        lepre = 0
    return lepre, leprergia, lep_tired



winner:bool = False
weather:int = 0
pioggia:bool = 0

print("BANG !!!!! AND THEY'RE OFF !!!!!")
while winner == False:
    percorso:list[str] = ["_" for i in range(1, 71)]
    weather += 1
    if weather > 9:
        weather = 0
        pioggia:int = random.getrandbits(1)

    tartaruga, tartamina, tarta_tired = tarta_choice(tartaruga, tartamina)
    lepre, leprergia, lep_tired = lep_choice(lepre, leprergia)

    if (tartaruga+1) in modifiers:
        print(f"THE TORTOISE STEPPED ON A {modifiers[tartaruga+1][1]}!!!")
        tartaruga += modifiers[tartaruga+1][0]
        if tartaruga > 69:
            tartaruga = 69
    if (lepre+1) in modifiers:
        print(f"THE HARE STEPPED ON A {modifiers[lepre+1][1]}!!!")
        lepre += modifiers[lepre+1][0]
        if lepre > 69:
            lepre = 69        

    if pioggia == True:
        print("IT'S RAINING!!!")
        if tartaruga > 0\
        and tarta_tired == False:
            tartaruga -= 1
        if lepre > 1\
        and lep_tired == False:
            lepre -= 2
    else:
        print("THE SUN SHINES!!!")

    if tartaruga > 69 and lepre > 69\
    and tartaruga == lepre:
        winner = True
        print("IT'S A TIE")
        continue
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

    print(percorso)
    view_pos(tartaruga, lepre)