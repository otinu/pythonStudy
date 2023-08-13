# 【4:Pythonのクラス】


class Parent:
    def __init__(self, b):
        self.b = b

    def w(self):
        return self.b


class Child(Parent):
    def __init__(self, a, b):
        self.a = a
        super().__init__(b)  # 👈super()ではなく、super().__init__()が正解


child = Child("Hello", "World")
print(f"{child.a} {child.b}")
