import random

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


# 下記のような記述をすると、タプルになる
t = (2,)
print(t)
# ⇒ (2,)

# この記述だとタプルではなく、int
t = (2)
print(t)
# ⇒ 2


# 文字列連結①
a = "A"
b = "B"
c = "C"
print(a,b,c) # ⇒ A B C    ##空白文字も含まれる点に注意
print(a + b + c) # ⇒ ABC
print(a,b + c) # ⇒ A BC   ## ","で連結すると間に空白文字が入る

# 文字列連結②

# joinを使うことでリスト内の要素を容易に連結できる
# ⇒書き方が独特なため注意が必要
text_list = [a, b, c]
print(", ".join(text_list))


# randomモジュール ================================================

# 【参考】https://www.delftstack.com/ja/howto/python/random-integers-between-range-python/


## randint()
x = random.randint(0,10)
print(x)
# ⇒ 0～10までの整数をランダム生成

## randrange()
x = random.randrange(0,6,2)
print(x)
# ⇒ 0,2,4 のいずれかをランダム生成
#  ⇒0～5までの範囲のうち、2で割り切れる値だけをランダム生成
# ※randint()は指定した範囲のNまでが対象なのに対し、randrange()はN-1まで(今回は5まで)が対象である点に注意

## sample()

sample_list = [0, 2, 4, 6]
x = random.sample(range(5),3)
print(x)
# ⇒ [4, 1, 3]や[2, 0, 1]など
# ⇒ 要素数が3で、各要素が0～4のいずれかの値をもつリストをランダム生成
# ⇒ 生成されるリスト内の要素は重複しない

y = random.sample(sample_list, 3)
print(y)
# ⇒ [2, 0, 6]や[0, 2, 4]など
# ⇒ 要素数が3で、sample_list内のいずれかの値をもつリストをランダム生成
# ⇒ 生成されるリスト内の要素は重複しない

# ※1 range()を使う場合、範囲がN-1までの点に注意
# ※2 第一引数の要素や範囲 < 第2引数の値とはできない
#     ⇒例えば、random.sample(range(2),3)では[0, 1, 1]や[1, 0, 1]など生成されるリスト内で重複する要素ができてしまうため