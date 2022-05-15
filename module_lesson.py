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
r = utils.say_twice("Hello") #該当パッケージ内のファイル名からの記述
print(r)

"""
# "*"でまとめて読み込むには_init_.pyに_all_の追加が必要
#    ⇒何が使われているのか分かりにくいため、非推奨
from lesson_package import *
print(utils.say_twice("Hello")) #該当パッケージ内のファイル名からの記述でOK
print(fish.swim())
"""