#eng esp
def lang(x):
    t = 0
    s = 0
    for i in range(len(x)):
        print(x[i])
        if x[i] == ("t" or "T"):
            t = t + 1
        elif x[i]== ("s" or "S"):
            s = s + 1 
    print(t)
    print(s)
    if t > s:
        bleh = "prob english" 
    elif s > t:
        bleh = "prob french"
    elif s == t:
        bleh = "prob french"
    
    print(bleh) 
    
#possion = input('gimmie words.:') 




#lang(possion)


#parking 

import random

options = ["c", "."]

spots = int(input("how many lots are being dealt with?:")) 



yest = []
for i in range (spots):
    t = random.choice(options) 
    yest.append(t)
print(yest) 


tday = []
for i in range (spots):
    t = random.choice(options) 
    tday.append(t)
print(tday)
        


count = 0 
for i in range(spots):
    if yest[i] == "c"and tday[i] == "c":
        count += 1
    else:
        count = 0  
print(count)