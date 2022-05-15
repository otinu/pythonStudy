"""
# ①importして、フルパスで読み込む方法
# メリット: 定義元が分かりやすい
# デメリット: コードが長くなる

import lesson_package.utils

r = lesson_package.utils.say_twice("aloha")
print(r)
"""
#from-importで読み込む方法
from lesson_package import utils
r = utils.say_twice("Hello") #該当パッケージ内のファイル名からの記述でOK
print(r)
