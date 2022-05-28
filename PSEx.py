import math

# 文字コード=================================
"""
# ファイルの冒頭で文字コードの指定が可能
# -*- coding: cp1252 -*-

print("ã�“ã‚“ã�«ã�¡ã‚�")
"""
#====inport===================================
"""
インポートの順番

①ビルトインモジュール(標準ライブラリ)
②サードパーティライブラリ
③自作ライブラリ

"""
# 負の要素番号================================

## 負の要素番号の場合、先頭は-1から
test_text = "ABCDE"
print(test_text[-1]) # ⇒ E

## 範囲指定する場合、どちらもN-1番目までを取得
print(test_text[0:2]) # ⇒ AB
print(test_text[-3:-1]) # ⇒ CD

# forとループの関係===========================

## range(x, y)ではx < yの間、x～yまでループをする。
## ⇒このため、内側1回目のループは(2,2)となり、ループ内は実行されずに終了する
for n in range(2, 10):
    for x in range(2 ,n):
        print("nは" + str(n) + ", xは" + str(x))
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else: #☆①
        print(n,'is a prime number')

"""
2 is a prime number
nは3, xは2
3 is a prime number
nは4, xは2
4 equals 2 * 2
nは5, xは2
nは5, xは3
nは5, xは4
5 is a prime number
"""
# enumerate(インデックス付きループ)=======================

# カウントを付きでループを回すことができる
# ⇒Rubyのwith_index()と同じ
index = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(index):
    print(index, name)

# enumerate()を使わない場合は下記のようになる
books = ["mero", "waga", "rasyo", "yuki"]
for i in range(len(books)):
    print(i, books[i])

"""
# 開始する要素番号の変更も可能

#要素番号1000から開始
for index, name in enumerate(index, start - 1000):
    print(index, name)

"""

# 比較の判定===============================================

# 文字列の比較では大文字・小文字の区別はせず、辞書順に大小が判定される
print("Word" > "world")
# ⇒ False

# format()================================================

# math.eはは自然対数の底 (e)、約 2.718
print(math.e)

# {0:.5f} ⇒ 「0番目の引数を使う : 小数点第5位まで」
# {1:.3f} ⇒ 「1番目の引数を使う : 小数点第3位まで」
## どちらも整数部に制限はなし
print('{1:.3f}, {0:.5f}'.format(math.pi, math.e))



