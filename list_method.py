# range関数--------------------------------------------------------------
#リストを作らずに、好みの回数だけループさせることができる

# 1.先頭から何番目スタートにするか
# 2.最大はいくつまでか
# 3.いくつ飛ばすか
for i in range(2,10,3):
    print(i)
print("==============")

# 「ブロック変数を使いません」を明示するには"_"を使う
for _ in range(5):
    print("hello")

# enumerate関数-----------------------------------------------------------
#カウンターを利用したい場合、カウント用の変数を定義しなくてもカウントができる
for i, character in enumerate(["a", "b", "c"]):
    print(i, character)


# zip関数--------------------------------------------------------------
#下記コメントアウトにブロック変数を複数回記述させないことで可読性を高められる
characters1 = ["a", "b", "c"]
characters2 = ["d", "e", "f"]
characters3 = ["g", "h", "i"]

"""
for i in range(len(characrers1)):
    print(characters1[i], characters2[i], characters3[i])
"""

for character1, character2, character3 in zip(characters1, characters2, characters3):
    print(character1, character2, character3)