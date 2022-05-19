class Car(object):
    def run(self):
        print("Car run")

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print("auto run")

car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

# TeslaCarはスーパークラスのrun()も自身のauto_run()も呼び出せる
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

class Ship(object):
    def run(self):
        print("Ship run")

# 多重継承================

class sugoiCar(Car, Ship):
    def sugoi(self):
        print("水陸両用で走ります")

sugoi = sugoiCar()
sugoi.run()