#eng esp
def lang(x):
    t = 0
    s = 0
    for i in range(len(x)):
        if x[i] == ("t" or "T"):
            t = t + 1
        elif x[i]== ("s" or "S"):
            s = s + 1 
    
    if t > s:
        bleh = "prob english" 
    elif (s > t) or (s == t):
        bleh = "prob french"
    print(f"there are {t} t's amd {s} s's, therfore this is {bleh}") 


    
#possion = input('gimmie words.:') 


#lang(possion)


#parking 
def parking(y ,t):
    cc = 0 
    where = []
    for i in range(len(y)):
        if y[i] == "c" and t[i] == "c":
            cc += 1
            where.append(i)
    print(y)
    print(t)
    print(f"{cc} spots are taken in spots {where}") 
parking("c...c..c.ccccc", "c..cc.c.ccc.cc") 
