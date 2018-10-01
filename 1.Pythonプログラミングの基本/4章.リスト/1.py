def spam(divide_by) :
    try:
        return 42 / divide_by
    except :
        print("エラー: 不正な引数です")

print(spam(2))
print(spam(12))
print(spam("asdff"))
print(spam(1))
