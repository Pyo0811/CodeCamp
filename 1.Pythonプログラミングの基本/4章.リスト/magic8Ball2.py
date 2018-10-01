from random import *

messages = ["確かにそうだ",
            "間違いなくそうだ",
            "はい",
            "なんとも。もういちどやってみて",
            "あとでもう一度きいてみて",
            "集中してもう一度きいてみて",
            "私の答えはノーです",
            "見通しはそれほど良くない",
            "とても疑わしい"]

print(messages[randint(0, len(messages) -1 )])
