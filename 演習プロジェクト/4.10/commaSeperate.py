def comma_seperate(eggs) :
    sausage = ""
    for i in range(len(eggs)) :
        if len(eggs) == 1 :
            sausage = sausage + eggs[i]
        else :
            if i == len(eggs) -1 :
                sausage = sausage + ("and " + eggs[i])
            else :
                sausage = sausage + (eggs[i] + ", ")
    return sausage    
    
    
    
spam = ['apples', 'bananas', 'tofu', 'cats','tiger', 'monkey', 'shark']
print(comma_seperate(spam))
spam = ['apples', 'bananas']
print(comma_seperate(spam))
spam = ['apples']
print(comma_seperate(spam))
spam = []
print(comma_seperate(spam))
