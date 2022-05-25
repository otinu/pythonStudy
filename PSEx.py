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
for n in range(2, 10):
    # 外側ループ ⇒ 内側ループに入るタイミングで、内側ループに属するelseが実行 ☆①
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