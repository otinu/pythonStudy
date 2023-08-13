# 【16:テスト】
from unittest.mock import Mock


mock = Mock()
mock.return_value = 3.14
# int(mock) # ⇒ エラー
# print(int(mock())) # ⇒ 3

mock.__int__ = Mock(return_value=5)
print(int(mock))  # ⇒ 5

# int(mock)は9行目のような形でセットしないとエラーになる
