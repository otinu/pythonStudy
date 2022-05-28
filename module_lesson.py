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

""" Pythonチュートリアル==================================================================================


モジュール名はprint(importしてるモジュール名.__name__)とすることでモジュール名を取得できる
# ⇒単に「importしてるモジュール名を文字列で指定すてばいい」とも思えるものの、処理の仕様上、中身が動的である場合には必要

例えばAさんとBさんはそれぞれパッケージaとパッケージbを作り、それぞれの中に関数名my_functionを作っていたとする。
その場合、Cさんが両方のモジュールをインポートしてから、a.my_function | b.my_function　と記述することで区別することができる。
 ⇒AさんとBさんは他の人のモジュールを気にせず、好きな関数名を命名することができる
"""