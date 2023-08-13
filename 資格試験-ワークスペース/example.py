def add(a, b):
    """2つの整数の合計値を取得する"""
    # テストを失敗させるために意図的にバグを入れる
    if a == 1 and b == 3:
        return 3
    elif a == 3 and b == 3:
        return 7
    return a + b
