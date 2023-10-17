Cube = [[[1,2,3],
         [4,5,6],
         [7,8,9]],
         
        [["A","B","C"],
         ["D","E","F"],
         ["G","H","I"]],
          
        [["R","S","T"],
         ["U","V","W"],
         ["X","Y","Z"]]]

def Rotate(Layer : list, Counter_Clockwise : bool):
    """returns a "rotated" List of the input according to standard rubiks cube notation"""
    if Counter_Clockwise == False:
        X = Layer[-2:]
        Y = Layer[:-2]
        X.extend(Y)
        return X

def get_layers(Layer : str, Cube : list):  ###  Read  ###
    """returns a list consisting of all elements of the specified layer according to standard rubiks cube notation"""
    Output = []
    if Layer == "F":
        Output = Cube[0][0]
        Output.append(Cube[0][1][2])
        Output.extend(Cube[0][2][::-1])
        Output.append(Cube[0][1][0]) 
        return Output
    elif Layer == "U":
        Output = Cube[2][0]
        Output.append(Cube[1][0][2])
        Output.extend(Cube[0][0][::-1])
        Output.append(Cube[1][0][0])
        return Output
    elif Layer == "E":
        Output = Cube[0][1]
        Output.append(Cube[1][1][2])
        Output.extend(Cube[2][1][::-1])
        Output.append(Cube[1][1][0])
        return Output
    elif Layer == "S":
        Output = Cube[1][0]
        Output.append(Cube[1][1][2])
        Output.extend(Cube[1][2][::-1])
        Output.append(Cube[1][1][0])
        return Output
    elif Layer == "B":
        Output = Cube[2][0][::-1]
        Output.append(Cube[2][1][0])
        Output.extend(Cube[2][2])
        Output.append(Cube[2][1][2])
        return Output
    elif Layer == "D":
        Output = Cube[2][2][::-1]
        Output.append(Cube[1][2][0])
        Output.extend(Cube[0][2])
        Output.append(Cube[1][2][2])
        return Output
    elif Layer == "R":
        return [Cube[0][0][2],
                Cube[1][0][2],
                Cube[2][0][2],
                Cube[2][1][2],
                Cube[2][2][2],
                Cube[1][2][2],
                Cube[0][2][2],
                Cube[0][1][2]]
    elif Layer == "L":
        return [Cube[2][0][0],
                Cube[1][0][0],
                Cube[0][0][0],
                Cube[0][1][0],
                Cube[0][2][0],
                Cube[1][2][0],
                Cube[2][2][0],
                Cube[2][1][0],]
    elif Layer == "M":
        return [Cube[2][0][1],
                Cube[1][0][1],
                Cube[0][0][1],
                Cube[0][1][1],
                Cube[0][2][1],
                Cube[1][2][1],
                Cube[2][2][1],
                Cube[2][1][1],]
    else:
        print(f"{Layer} is not defined")
print(f" Cube ::: {Cube}")
print(f" get layers ::: {get_layers('F',Cube)}")
print(f' Rotate ::: {Rotate(get_layers("F",Cube), False)}')

Layer = get_layers("F",Cube)


#Test = ["F","B","R","L","U","D","M","E","S"]
#for i in Test:
#    print(f"{i} ::: {get_layers(i, Cube)}")

#print(Rotate([1,2,3,4,5,6,7,8,9], False))

def write_Layers(Rot_Layer : list, Layer : str, Cube : list):
    """Overwrites the specified layer in the cube, effectively turning it"""
    if Layer == "F":
        Cube[0][0][0] = Rot_Layer[0]
        Cube[0][0][1] = Rot_Layer[1]
        Cube[0][0][2] = Rot_Layer[2]
        Cube[0][1][2] = Rot_Layer[3]
        Cube[0][2][2] = Rot_Layer[4]
        Cube[0][2][1] = Rot_Layer[5]
        Cube[0][2][0] = Rot_Layer[6]
        Cube[0][1][0] = Rot_Layer[7]
    elif Layer == "U":
        Cube[2][0][0] = Rot_Layer[0]
        Cube[2][0][1] = Rot_Layer[1]
        Cube[2][0][2] = Rot_Layer[2]
        Cube[1][0][2] = Rot_Layer[3]
        Cube[0][0][2] = Rot_Layer[4]
        Cube[0][0][1] = Rot_Layer[5]
        Cube[0][0][0] = Rot_Layer[6]
        Cube[1][0][0] = Rot_Layer[7]
    elif Layer == "E":
        Cube[0][1][0] = Rot_Layer[0]
        Cube[0][1][1] = Rot_Layer[1]
        Cube[0][1][2] = Rot_Layer[2]
        Cube[1][1][2] = Rot_Layer[3]
        Cube[2][1][2] = Rot_Layer[4]
        Cube[2][1][1] = Rot_Layer[5]
        Cube[2][1][0] = Rot_Layer[6]
        Cube[1][1][0] = Rot_Layer[7]
    elif Layer == "S":
        Cube[1][0][0] = Rot_Layer[0]
        Cube[1][0][1] = Rot_Layer[1]
        Cube[1][0][2] = Rot_Layer[2]
        Cube[1][1][2] = Rot_Layer[3]
        Cube[1][2][2] = Rot_Layer[4]
        Cube[1][2][1] = Rot_Layer[5]
        Cube[1][2][0] = Rot_Layer[6]
        Cube[1][1][0] = Rot_Layer[7]
    elif Layer == "B":
        Cube[2][0][2] = Rot_Layer[0]
        Cube[2][0][1] = Rot_Layer[1]
        Cube[2][0][0] = Rot_Layer[2]
        Cube[2][1][0] = Rot_Layer[3]
        Cube[2][2][0] = Rot_Layer[4]
        Cube[2][2][1] = Rot_Layer[5]
        Cube[2][2][2] = Rot_Layer[6]
        Cube[2][1][2] = Rot_Layer[7]
    elif Layer == "D":
        Cube[2][2][2] = Rot_Layer[0]
        Cube[2][2][1] = Rot_Layer[1]
        Cube[2][2][0] = Rot_Layer[2]
        Cube[1][2][0] = Rot_Layer[3]
        Cube[0][2][0] = Rot_Layer[4]
        Cube[0][2][1] = Rot_Layer[5]
        Cube[0][2][2] = Rot_Layer[6]
        Cube[1][2][2] = Rot_Layer[7]
    elif Layer == "R":
        Cube[0][0][2] = Rot_Layer[0]
        Cube[1][0][2] = Rot_Layer[1]
        Cube[2][0][2] = Rot_Layer[2]
        Cube[2][1][2] = Rot_Layer[3]
        Cube[2][2][2] = Rot_Layer[4]
        Cube[1][2][2] = Rot_Layer[5]
        Cube[0][2][2] = Rot_Layer[6]
        Cube[0][1][2] = Rot_Layer[7]
    elif Layer == "L":
        Cube[2][0][0] = Rot_Layer[0]
        Cube[1][0][0] = Rot_Layer[1]
        Cube[0][0][0] = Rot_Layer[2]
        Cube[0][1][0] = Rot_Layer[3]
        Cube[0][2][0] = Rot_Layer[4]
        Cube[1][2][0] = Rot_Layer[5]
        Cube[2][2][0] = Rot_Layer[6]
        Cube[2][1][0] = Rot_Layer[7]
    elif Layer == "M":
        Cube[2][0][1] = Rot_Layer[0]
        Cube[1][0][1] = Rot_Layer[1]
        Cube[0][0][1] = Rot_Layer[2]
        Cube[0][1][1] = Rot_Layer[3]
        Cube[0][2][1] = Rot_Layer[4]
        Cube[1][2][1] = Rot_Layer[5]
        Cube[2][2][1] = Rot_Layer[6]
        Cube[2][1][1] = Rot_Layer[7]
    else:
        print(f"{Layer} is not defined")

def Turn_Cube(Move : str, Counter_Clockwise : bool ,  Cube : list):
    write_Layers(Rotate(get_layers(Move,Cube), Counter_Clockwise),Move,Cube)

