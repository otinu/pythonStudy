class Person(object):

    # __init__でデフォルトコンストラクタを作成
    ### 引数にselfは必ず必要
    ### 実質的にnameが第一引数
    def __init__(self, name):

        ### クラスフィールドのnameに値を入れる
        self.name = name

    #デストラクタを作成
    #    ⇒インスタンスが破棄されるときに自動的に実行される
    def __del__(self):
        print("See you")

    def who_are_you(self):
        ### 引数なしでも、クラスフィールドのnameに値が入っていれば呼び出せる
        print("I'm " + self.name)

person = Person("tinu")
person.who_are_you()
# person.say_something()



# クラス変数

class meal(object):
    main = "米" # 一見、フィールドに見えるものの、これがクラス変数

lunch = meal()
lunch.main = "パン"
print(lunch.main)

dinner = meal()
dinner.main = "麺"
print(dinner.main)
print("また" + lunch.main)