def is_phone_number(text) :
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 は電話番号:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi は電番号:')
print(is_phone_number('Moshi moshi'))

message = "明日415-555-1011に電話してください。オフィスは415-555-9999です。"
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("電話番号が見つかりました: " + chunk)
print("完了")

# shell typing
# >>> import re
# >>> phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> mo = phone_num_regex.search('私の電話番号は415-555-4242です。')
# >>> print('電話番号が見つかりました: ' + mo.group())
