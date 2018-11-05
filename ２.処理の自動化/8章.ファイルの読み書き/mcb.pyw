#! python3
# mcb.pyw - クリップボードのテキストを保存'復元
# Usage:
# py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
# py.exe mcb.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys  

mcb_shelf = shelve.open('mcb')  
# クリップボードの内容を保存 
if len(sys.argv) == 3:
     command = sys.argv[1].lower()
     key = sys.argv[2]
     if command == 'save':
         mcb_shelf[key] = pyperclip.paste()
     elif command == 'delete':
         del mcb_shelf[key]

elif len(sys.argv) == 2:
     # キーワード一覧と内容の読み込み
     if sys.argv[1].lower() == 'list':
         pyperclip.copy(str(list(mcb_shelf.keys())))
     elif sys.argv[1].lower() == 'delete':
         mcb_shelf.clear()
     elif sys.argv[1] in mcb_shelf:
         pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
