# 【9:データ型とアルゴリズム】

from collections import defaultdict

di = defaultdict(list)
di["test"].append("value")
di["test2"]
print(list(di.items()))
# ⇒ [('test', ['value']), ('test2', [])]

# これはエラーにならない
"""
di = defaultdict(dict)
di = defaultdict(int)
di = defaultdict(list)
"""

# これはエラーになる
"""
di = defaultdict(list()) 👈list()など()入れるのがダメ
"""
