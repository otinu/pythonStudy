# ifの末尾に「:」が入らない点に注意
result = [n for n in range(10) if n % 2 == 0]
print(result)
# ⇒ [0, 2, 4, 6, 8]

# 辞書型をループするとき、ブロック変数の中には各キーが入っている点に注意
fishs = {"tinu": "黒鯛", "gure": "クロ", "bera": "キュウセン"}
for fish in fishs:
    print(fishs[fish])
    # ⇒ 黒鯛クロキュウセン

#下記のように、複数の代入を一度に実行する処理を【多重代入】という
tajyu1, tajyu2 = 1, 2

# returnなしで関数を呼び出した場合、返り値はNone
def no_return():
    global no_number
    no_number = 1000

print(no_return())
# ⇒ None

# format()を使うよりも、文字列先頭にfを付ける方法のほうが読みやすいと思う
greet = "Hay,"
who = "Tom"
greeting = "{}{}! Have a good day!".format(greet, who)
print(greeting)

greeting = f"{greet}{who}! Have a good day!"
print(greeting)

# else節はexcept節とfinally節の間に記述
# 「else:」と":"を忘れないよう注意
result = None
try:
    result = 5 / 0
except ZeroDivisionError:
    print("ZeroDiv")
else:
    print("else")
finally:
    pass

# Pythonで対話モードを終了させるコマンドは「quit()」
# ⇒ "()"を付ける点に注意

# IPythonは「pip install ipython」でインストールし、「python -m IPython」で対話モードを起動できる
