def comma_seperate(list) :
    fruit1, fruit2, food, animal = list
    return str(fruit1) + ", " + str(fruit2) + ", " + str(food)+ ", and " + str(animal)


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_seperate(spam))
