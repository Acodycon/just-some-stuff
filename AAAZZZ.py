Pin = 36435

#   1   2   3

#   4   5   6

#   7   8   9

#       0

Counter = 0
def recursive_loop(n):
    global Counter
    Counter += 1
    print(Counter)
    if n == 0:
        return Counter
    else:
        return recursive_loop(n - 1)


def get_pins(observed):
    NumPad = [[1,2,3],[4,5,6],[7,8,9]]  # # # 
    Possibilities = [[1,2,4],[2,1,3,5],[3,2,6],[4,1,5,7],[5,2,4,6,8],[6,3,5,9],[7,4,8],[8,5,7,9,0],[9,6,8],[0,8]]
    Output = []
    string = str(observed) # = "36435"
    n = len(str(observed))
    i = 0
    Possies = ""
    for j in range(len(Possibilities[int(string[i]) - 1])):  # 3
        Possies += str(Possibilities[int(string[i]) - 1][j])
        
        for k in range(len(Possibilities[int(string[i + 1]) - 1])): # 4
            Possies += str(Possibilities[int(string[i + 1]) - 1][k])
            
            for l in range(len(Possibilities[int(string[i + 2]) - 1])): # 4
                Possies += str(Possibilities[int(string[i + 2]) - 1][l])
                
                for m in range(len(Possibilities[int(string[i + 3]) - 1])): # 3
                    Possies += str(Possibilities[int(string[i + 3]) - 1][m])
                    
                    for n in range(len(Possibilities[int(string[i + 4]) - 1])): # 5
                        Possies += str(Possibilities[int(string[i + 4]) - 1][n])
                        Output.append(Possies)
                        Possies = Possies[:-1]
                    Possies = Possies[:-1]
                Possies = Possies[:-1]
            Possies = Possies[:-1]
        Possies = Possies[:-1]
    return Output

    
#print(get_pins(Pin))
#print(recursive_loop(10,2))
print(recursive_loop(19))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#print(factorial(5))