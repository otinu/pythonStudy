# [Ctrl]+[c]キーなどでユーザーがプログラムに割り込みをかけると、KeyboardInterrupt例外が発生

# パーサ（構文解釈器）は違反のある【ファイル名 と 行番号】を表示し、最初にエラーが検知された点に下線が引かれる。エラーは矢印より前のトークンが原因である。

# 【python3 script.py one two three four five】を実行した際、コマンドライン引数の先頭は「script.py」
# ⇒print(sys.args[0])の出力は「script.py」

# https://techacademy.jp/magazine/35730
# モジュールprocessing を用いることで、JavaやPythonで近代的なデジタルアートを再現することができる
# time/timeit モジュールで処理時間の計測が可能

# loggingモジュールのメッセージの優先度
# ⇒CRITICAL、ERROR、WARNING、INFO、DEBUG

# モジュールの名前空間は、インタプリタが終了するまで残ります。
# 関数のローカルな名前空間は、関数が呼び出されたときに作成され、
# 関数から戻ったときや、関数内で例外が送出され、かつ関数内で処理されなかった場合に削除されます。

# 対話型インタープリタでは文字列は引用符に囲まれ、特殊文字はバックスラッシュでエスケープされた状態で出力される。
# print()関数では全体を囲む引用符が除去され、エスケープ文字や特殊文字がプリントされた状態で出力される。

# Pythonのバージョンをコードで確認する場合は、print(sys.version) を使う

# データの代表値を取得======================================

"""
# 純粋にPythonで取得するにはstatisticsモジュールのインポートが必要
import statistics

data = [1,10,15,20,25,30,35]

# 平均値
rslt1 = statistics.【A】(data)

# 中央値
rslt2 = statistics.【B】(data)

# 分散値
rslt3 = statistics.【C】(data)


# その他、numpyパッケージのdescribe()では平均値や中央値を一気に取得できる

"""

# 演算子とオペランド==========================================

# a = 2 + 3

## 演算子(オペレーター)  ⇒ 「+」のこと
## オペランド            ⇒ 「2」や「3」のこと


# べき乗の優先順位====================

# べき乗は右から計算されていく

### ① 1の3乗
### ② 2の1乗
print(2 ** 1 ** 3)

### べき乗以外は通常通り、左から計算
### ((48/6の整数部) / 4)の整数部
print(48 // 6 // 4)

print("===================================")

# ひっかけ===============================

# 一見、argには3が代入されているように見えてしまうが、これはキーワード引数
# 関数呼び出し時には引数で2が指定されるため、argには2が入ることになる
zuru = 2
def zurui_kannsuu(arg = 3):
    zuru = 4
    zuru = 5
    print(arg)

zurui_kannsuu(zuru)

# ループを1行で書いて、リストを作る=======================

# for-inで作る
cubes = [a ** 3 for a in range(5)]
print(cubes)

# lambdaで作る
cubes = list(map(lambda a: a ** 3, range(5)))
print(cubes)

# ループを1行で書いて、2次元リストを作る=======================

# for-inで作る
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
power = [[row[i] for row in matrix] for i in range(3)]
print(power)

# list()とzipで作る
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
power = list(zip(*matrix))
print(power)