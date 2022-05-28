# [Ctrl]+[c]キーなどでユーザーがプログラムに割り込みをかけると、KeyboardInterrupt例外が発生

# パーサ（構文解釈器）は違反のある【ファイル名 と 行番号】を表示し、最初にエラーが検知された点に下線が引かれる。エラーは矢印より前のトークンが原因である。

# 【python3 script.py one two three four five】を実行した際、コマンドライン引数の先頭は「script.py」
# ⇒print(sys.args[0])の出力は「script.py」


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