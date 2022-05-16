class Person(object):

    # __init__でデフォルトコンストラクタを作成
    ### 引数にselfは必ず必要
    ### 実質的にnameが第一引数
    def __init__(self, name):

        ### クラスフィールドのnameに値を入れる
        self.name = name

    def who_are_you(self):
        ### 引数なしでも、クラスフィールドのnameに値が入っていれば呼び出せる
        print("I'm " + self.name)

person = Person("tinu")
person.who_are_you()
# person.say_something()