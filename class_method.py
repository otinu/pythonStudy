class Person(object):
    kind = "human"

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

a = Person()
print(a.what_is_your_kind())
print(Person.kind)

### @classmethodがついていないと、オブジェクト生成なしに呼び出せない
print(Person.what_is_your_kind())