#Pythonの基本的なメソッドはbuiltinsパッケージ内で定義されている
import builtins
builtins.print("Hello World")

#使用頻度の高いsorted()の例
ranking = {
    "A": 100,
    "B": 85,
    "C": 95
}

# ①ソートする対象指定
# ②dictionary型のため、キーの取得を指定
# ③降順指定(デフォルトは昇順)
print(sorted(ranking, key = ranking.get, reverse = True))