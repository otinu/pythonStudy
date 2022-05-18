class Car(object):
    def run(self):
        print("super run")

class ToyotaCar(Car):

    def __init__(self, name = "N-BOX"):
        self.__name = name

    #ゲッター
    @property
    def get_name(self):
        return self.__name

    #セッター
    @get_name.setter
    def set_name(self, name):
        self.__name = name

car = ToyotaCar()
print(car.get_name)

car.set_name = "WBM"
print(car.get_name)