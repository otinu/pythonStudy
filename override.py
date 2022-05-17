class Car(object):
    def run(self):
        print("super run")

class ToyotaCar(Car):
    def run(self):
        super().run() #オーバーライド時でもsuper()を使って、呼び出せる

car = ToyotaCar()
car.run()