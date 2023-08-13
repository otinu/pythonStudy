from unittest.mock import MagicMock

# モックオブジェクトは直前に「9,10」の引数で呼び出されてる
m = MagicMock()
m(1, a=2)
m(3, b=4)
m(9, b=10)
# num = 1 + 2
m.assert_called_with(3, b=4)
# ⇒ エラー発生


# モックオブジェクトは直前に「3,4」の引数で呼び出されてる
m = MagicMock()
m(1, a=2)
m(3, b=4)
num = 1 + 2
m.assert_called_with(3, b=4)
# ⇒ エラーなし
