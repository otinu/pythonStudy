import math #☆①
from decimal import Decimal #☆②
import re #☆③
from struct import pack #☆④
from struct import unpack #☆④

#対話モード時に、最後に表示した式を格納している変数==============
# ⇒_(アンダバー)

# ビルドイン関数dir() ===========================================
# ⇒ モジュールが定義している名前を確認することができる。

# pyenv
# ⇒pyenvとは、pythonのバージョン管理が可能な仮想環境です。２系と３系で環境を切り替えたり、
#   プロジェクト毎に環境を切り替えたりすることが簡単にできる。

# IPython
# ⇒対話型インタプリタ
#  ⇒やりとりのヒストリ情報は.python_historyに保存される

# math.piは円周率の値をもっている================================
print(math.pi)

# mathはインポートが必要 ☆①
# 細かすぎるときはフォーマット可能
# ⇒%〇.△f
#  ⇒〇が整数・△が小数点
#  ⇒〇と△の各数値は「何桁まで表示するか」を表す
test = math.pi * 5
print("出力結果:")
print('円周率を5倍すると%2.4fである。'%test)

# decimal型(固定小数)やfloat型(浮動小数)=========================
    #NG
    #print(type(5.1f))
print(int(10.45))
print(float(10.45))

# Decimalはインポートが必要 ☆②
# Decimalはクォテーションで囲わないと誤差が出てしまう
print(Decimal(10.45))
print(Decimal("10.45"))

# 正規表現=======================================================
# 正規表現はreをインポート ☆③
URL = "http://www.amazon.co.jp/dp/B07T9TCPZX"
pattern = "https?://[^/]+/"
res = re.match(pattern, URL)
print(res.group())

# バイナリデータの取り扱い=======================================
# バイナリデータの取り扱いはstructをインポート ☆④

### "h"は2バイトで表現
data = pack('hhh', 1, 2, 3)
print(type(data))
print(data)
# ⇒b'\x01\x00\x02\x00\x03\x00'

### "l"は4バイトで表現
data2 = pack('llh', 1, 2, 3)
print(type(data2))
print(data2)
# ⇒b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00'

print(unpack("hhh", data))
#print(unpack("lll", data)) #アンパックする際はバイト数を合わせる必要がある

#range関数の使い方==================================================

## forとの組み合わせ=====

### 昇順
for i in range(3):
    print(i)
### 降順
for j in reversed(range(4)):
    if j == 3:
        print("ikuzetakao!!" + str(j) + ",")
    elif j > 0:
        print(str(j) + ",")
    else:
        print("ゴーシュ―と")

##  listとの組み合わせ
print(list(range(5)))

## forと組み合わせないとrangeは本来の機能をしない
print(range(3))