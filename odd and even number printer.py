import time
Even_Odd = input("Would you like to print (even) or (odd) numbers ? ")
print("In what range would you like to print all " + Even_Odd + " numbers ? ")
limit1 = int(input("limit 1: "))
limit2 = int(input("limit 2: "))
if Even_Odd == "even" and not(limit1 % 2 == 0):
    limit1 += 1
if Even_Odd == "even" and not(limit2 % 2 == 0):
    limit2 += 1
if Even_Odd == "odd" and limit1 % 2 == 0:
    limit1 += 1
if Even_Odd == "odd" and limit2 % 2 == 0:
    limit2 += 1
up_down = input("Whould you like to count (up) or (down) ? ")
if limit1 < limit2:
    start = limit1
    stop = limit2
else:
    start = limit2
    stop = limit1
if up_down == "up":
    stop += 2
    step = 2
else:
    start, stop = stop, start - 2
    step = -2

for a in range(start,stop,step):
    print(a)
    time.sleep(0.05)