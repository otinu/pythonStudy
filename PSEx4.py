"""
[ 実行結果 ]
Need Speed?
I'm Saya.
Need Speed?
I'm David.

[ コード ]
class kusanagi():
    def s(self):
        print("Need Speed?") 　 …★a　

        # 【C】の部分が実行された際にはwexal().m() のようになり、オーバーライドされたm()が呼び出される
        【A】(self.m() )
    def m(self):
        print("I'm Saya.")

class wexal(kusanagi):

        #オーバーライドしている
        def 【B】 (m(self) ):
            print("I'm David.")

k = kusanagi()
w = wexal()
k.s()
w.【C】 (s() )
"""