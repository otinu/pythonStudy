from collections import deque # ☆①

# round()=============================================
round_data = 0.1414210356
### 第二引数が0のときは、小数点第一位が0になるため注意
print(round(round_data, 2))
print(round(round_data + 1, 0))

# zip()===============================================

zip_data = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
]
print(zip_data)
# ⇒[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
print(list(zip(*zip_data)))
# ⇒[('A', 'D', 'G'), ('B', 'E', 'H'), ('C', 'F', 'I')]

# print()==============================================

###Pythonでは下記のような記述でもコンパイルに成功する
a = 2
b = 5
c = 3.0 + b, 5 * a
print(c)
# ⇒(8.0, 10)

# 例外時のメッセージ====================================

try:
    ### 例外を発生させる際にメッセージを入れる
    raise Exception("開始前","Exception発生")
    print("開始")
except IOError as msg:
    print("IOError発生:",msg.args[0])
except Exception as msg:
    ### argsの中にリストで入っている
    print("予期せぬ問題発生:",msg.args[1])
else:
    print("Else表示")

# sysモジュール===========================================

# コマンドライン引数を扱うことが可能
"""
import sys

print(sys.argv)
print(sys.argv[1])
"""

# コンパイル後のファイル===================================

# コンパイル済のファイルの拡張子は.pyc になる
# コンパイル済のモジュールは_pycache_に保存される


# リストで使えるメソッド===================================

## extend()========

memo = ['玉ねぎ', ['コーラ', 'オレンジジュース']]
mother_memo = ["カレールウ","にんじん", "じゃがいも", "豚肉"]
memo.extend(mother_memo)
print(memo)
# mother_memoを要素毎に分解してmemoにつなげられている
#⇒['玉ねぎ', ['コーラ', 'オレンジジュース'], 'カレールウ', 'にんじん', 'じゃがいも', '豚肉']

## pop(), popleft()=========

fishers = ["tinu", "kiss", "gure", "tyariko"]

first_catch = fishers.pop()
print(first_catch)
# ⇒tyariko

# ☆① collectionsからdequeのインポートが必要
second_catch = deque(fishers).popleft()
print(second_catch)
# ⇒tinu




