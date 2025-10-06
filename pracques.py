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
    





lang("Mason part à la chasse aux poissons non vidés à l'aube.")


#parking 




