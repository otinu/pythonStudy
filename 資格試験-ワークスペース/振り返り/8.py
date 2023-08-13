# 【9:データ型とアルゴリズム】
import itertools

liA = list(itertools.product("AB", "xy"))
print(liA)
# ⇒  [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')]

# 他の3つは、そもそもエラーになる
"""
liB = list(itertools.permutations("AB", "xy"))
liC = list(itertools.combinations("AB", "xy"))
liD = list(itertools.combinations_with_replacement("AB", "xy"))
"""
