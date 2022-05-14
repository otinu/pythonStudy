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