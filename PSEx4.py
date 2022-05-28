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

# アノテーションは「返すべき型が何の型か」を伝えるためにある
# 開発者から開発者への注意喚起だけであって、警告などは発生されない
def annotation_sample() -> int:
    sample_date = 100
    dammy_text = "間違った返り値"

    # dammy_textは開発者の意図した型ではないものの、返すことはできる

    ## return を2つ書いてもエラーにはならない様子(ただし、返るのは最初のreturnだけ)
    return sample_date
    return dammy_text
print(annotation_sample())

# returnで処理を終了した際の戻り値はNoneになる
def test_return():
    return
    print("returnしてるため、表示されません")
print(test_return())
# ⇒None

# 比較演算子の特殊チェーン================================

# PythonではANDを使わずに比較演算子を複数繋げることができる
# ⇒ただし、ANDを暗黙的に表現できるだけで、ORは通常通りに記述しないといけない様子？

## ① 5 > -5
## ② -5 < 5 - 9

## ① AND ② ⇒ True
print( 5 > -5 < 5 - 9)




