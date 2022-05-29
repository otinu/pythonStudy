# 抽象クラスの作成

from abc import ABC,abstractmethod

class Fish(ABC):

    # ※※抽象メソッドはクラスの一番上に定義する必要がある様子※※
        @abstractmethod
        def swim(self):
            pass

        def __init__(self, where = "bottom"):
            self.where = where

class Kiss(Fish):

    # Javaと同様、スーパークラスのコンストラクタが実行されてから自分のコンストラクタを実行する
    def __init__(self, where):
        print("Fisher should know Kiss lives in " + where)

    def bite(self):
        print("bite! bite!! Hurry,roll!!!!")

fish = Kiss("sandy beach")


