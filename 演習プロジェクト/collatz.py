def collatz(number) :
    if (number % 2) == 0 :
        return number / 2
    else :
        return 3 * number + 1


print("整数を入力してください。")
while True :
    try :
        number = int(input())
        collatz_number = collatz(number)
        if collatz_number == 1 :
            print(collatz_number)
            break
    except :
        print("整数値を入力するように示す")
