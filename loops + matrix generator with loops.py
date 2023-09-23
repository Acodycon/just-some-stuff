#usersolution = None
#solution = str(9 * 5)
#
#while not(usersolution == solution):
#    usersolution = input("What is 9 * 5 ? ")
#    if usersolution == solution:
#        print("Well done!")
#    else:
#        print("Are you stupid ? >:(")
#
#import time
#
#for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#    print(i)
#    time.sleep(.1)

while True:
    Input = input("Enter something: ")
    if Input != "":
        break                  # breaks the loop completely otherwise you can't break a while true loop

Number = "123-4123-433135-2323"

for i in Number:
    if i == "-":
        continue               # skips one iteration of the loop
    print(i , end = "")
print()


#Matrix Generator
import time

Type = None
type0 = "U"
type1 = "L"
type2 = "I"

while not(Type == type0 or Type == type1 or Type == type2):
    type = input("What type of Matrix would you like to generate ? (U)pper Δ, (L)ower Δ, (I)dentity ")
    Type = type.upper()
    if Type == "U":
        print("Upper Triangular Matrix")
    elif Type == "L":
        print("Lower Triangular Matrix")
    elif Type == "I":
        print("Identity Matrix")
    else:
        print("I'm sorry, but please use the letters in the brackets ! ")
        time.sleep(2)

rows = columns = int(input("What size should the Matrix have ? "))

if Type == "U":
    k = 0
    for i in range(rows):
        for j in range(columns):
            if j > k or j == k:
                print("1 ", end = "")
            else:
                print("O ", end = "")
        print()
        k += 1
    print("Done")
    quit
elif Type == "L":
    k = 0
    for i in range(rows):
        for j in range(columns):
            if j < k or j == k:
                print("1 ", end = "")
            else:
                print("O ", end = "")
        print()
        k += 1
    print("Done")
    quit
elif Type == "I":
    k = 0
    for i in range(rows):
        for j in range(columns):
            if j == k:
                print("1 ", end = "")
            else:
                print("O ", end = "")
        print()
        k += 1
    print("Done")
    quit
else:
    quit