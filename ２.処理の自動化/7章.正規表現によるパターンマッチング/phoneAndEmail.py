#! python3
# phoneAndEmail.py - クリップボードから電話番号とメアドを検索する

import pyperclip, re

phone_regex = re.complile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''',re.VERBOSE)
