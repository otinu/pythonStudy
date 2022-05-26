"""
# ファイルの冒頭で文字コードの指定が可能
# -*- coding: cp1252 -*-

print("ã�“ã‚“ã�«ã�¡ã‚�")
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