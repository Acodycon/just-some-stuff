# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python

array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]

def snail(snail_map):
    if 1 == 0:     # snail_map == [[]]:
        pass#return snail_map
    else:
        
        Output = []
        Length = len(snail_map)
        Number_of_Loops = None
        if len(snail_map) % 2 == 0:
            Number_of_Loops = int(len(snail_map) / 2)
        else:
            Number_of_Loops = int((len(snail_map) + 1) / 2)
        Current_Loop = 0
        for h in range(Number_of_Loops):
            Outer_Loop = [0 + Current_Loop,len(snail_map) - 1 - Current_Loop,len(snail_map) - 1 - Current_Loop,0 + Current_Loop]
            Loop_Counter = 0
            Out_Stays_The_Same = True
            for i in Outer_Loop:
                for j in range(0 + Current_Loop,(len(snail_map) - 1 - Current_Loop)):
                    if Out_Stays_The_Same == True:
                        if Loop_Counter >= 2:
                            Output.append(snail_map[i][-j + len(snail_map) - 1])
                            #print(f"what 0::: {i} {-j + len(snail_map) - 1}")
                        else:
                            Output.append(snail_map[i][j])
                            #print(f"what 1::: {i} {j}")
                    else:
                        if Loop_Counter >= 2:
                            Output.append(snail_map[-j + len(snail_map) - 1][i])
                            #print(f"what 2::: {-j + len(snail_map) - 1} {i}")
                        else:
                            Output.append(snail_map[j][i])
                            #print(f"what 3::: {j} {i}")
                Out_Stays_The_Same = not Out_Stays_The_Same                                                   
                Loop_Counter += 1
                #print(Loop_Counter)
            Current_Loop += 1
        if len(snail_map) % 2 != 0:
            Output.append(snail_map[int(len(snail_map) / 2)][int(len(snail_map) / 2)])
        return Output



print(snail(array))
print([1,2,3,1,4,7,7,9,8,7,7,4,])

import numpy as np

def ssnail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m

