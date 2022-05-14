#関数定義・呼び出しの基本形
def say_something():
    print("hi")

say_something()
print(type(say_something)) #型はfunction
#print(type(say_something()))    #NGな記述

#戻り値ありの関数定義
def fish():
    return "tinu"

some_fish = fish()
print(some_fish)

#引数一つの関数定義
def say_argument(word):
    print(word + "!!")

say_argument("Hello")

#呼び出し先で処理が可能な場合、エラーの警告が発生されない
    ###本来はint型の引数2つを想定して定義
def add_num(a: int, b: int) -> int:
    return "1" + "2"

r = add_num("a", "b") #string型の引数2つが与えられているのに実行できてしまう
print(r)
"""
#明らかに呼び出し先の関数で処理ができない場合にはエラー警告発生
r = add_num(a, b)
r = add_num(true, false)
"""

#プレースホルダを使って可読性高く記述することもできる
def menu(entree, drink, dessert):
    print("entree = ", entree)
    print("drink = ", drink)
    print("dessert = ", dessert)
###定義元と引数の順番が違くても正しく実行される
menu(drink = "coke", entree = "fruit", dessert = "cake")

#デフォルト引数を定義することが可能
def new_menu(entree = "beef", drink = "wine", dessert = "ice"):
    print("entree = ", entree)
    print("drink = ", drink)
    print("dessert = ", dessert)

print("オーダー入りました")
new_menu()
print("オーダー変更です")
new_menu(entree = "chiken")