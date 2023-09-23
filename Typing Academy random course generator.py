import random
import time

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
specials = [",",".","-",";",":","_","[","(",'"',"/","'","#","%","=","?","!"]
TAcharacerlimit = 2400


blocks = int(input("How many blocks of text do you want to generate ? "))
length = int(input("How long should each block of text be ? "))
Characters = length * blocks - 1
if Characters > TAcharacerlimit:
    print("TOO MANY CHARACTERS FOR TYPING ACADEMY ! ! ! ")
    time.sleep(1)
containnumber = input("should it also contain numbers ? ")
if containnumber == "yes":
    numberpercent = int(input("What percent of it should be numbers ? "))
else:
    numberpercent = 0
containspecials = input("should it also contain special characters ? ")
if containspecials == "yes":
    specialspercent = int(input("What percent of it should be special characters ? "))
else:
    specialspercent = 0

pn = numberpercent
ps = pn + specialspercent
pl = 100

for i in range(blocks):
    for j in range(length):
        r0 = random.randrange(1,101)
        if r0 <= pn:
            r1 = random.randrange(len(numbers))
            print(numbers[r1], end = "")
        elif pn < r0 <= ps:
            r1 = random.randrange(len(specials))
            print(specials[r1], end = "")
        else:
            r1 = random.randrange(len(letters))
            print(letters[r1], end = "")
print("DONE !")