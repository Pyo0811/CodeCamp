def collatz(number) :
    if (number % 2) == 0 :
        return int(number / 2)
    else :
        return int(3 * number + 1)


print("整数を入力してください。")
number = int(input())
while True :
    try :        
        number = collatz(number)
        print(number)
        if number == 1 :
            print(number)
            break
    except :
        print("整数値を入力するように示す")
