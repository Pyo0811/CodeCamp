cat_names = []
while True :
    print("猫" + str(len(cat_names) +  1) + "の名前を入力してください" +
          "(終了するにはEnterキーだけ押して下さい)")
    name = input()
    if name == "" :
        break
    cat_names = cat_names + [name] # リストの連結
print("猫の名前を次のとおり:")
for name in cat_names :
    print(" " + name )
