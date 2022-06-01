loc = "1"
def scope():
    print("ここからscope()実行===========================")
    loc = "2"   #scope()のloc
    def do_local():
        loc = "3"
    def do_nonlocal():
        nonlocal loc
        loc = "4"
    def do_global():
        #ここでは、「グローバル変数locと同一のlocです」と宣言していることになっている
        global loc
        loc = "5"

    do_local()
    print("【A】", loc)
    do_nonlocal()
    print("【B】", loc)
    do_global()
    print("【C】", loc)

    print("ここでscope()終了=============================")

print("【D】", loc, "    1行目のグローバル変数locを参照")
scope()
print("【E】", loc, "    1行目のグローバル変数locはdo_global()によって値が書き換えられている")

"""
【D】 1     1行目のグローバル変数locを参照
ここからscope()実行===========================
【A】 2    # 一つ外側にあるlocには反映されない
【B】 4    # 一つ外側にあるscope()のlocには反映されている
【C】 4    # 最外(グローバル変数)locには反映されているものの、scope()内のlocには反映されていない
ここでscope()終了=============================
【E】 5     1行目のグローバル変数locはdo_global()によって値が書き換えられている
"""




# 【参考】https://www.lifewithpython.com/2016/06/python-3-nonlocal.html

# 通常、関数内で定義したローカル変数内の値を書き換えてreturnしても、呼び出し元に返すことはできない
# ⇒nonlocalを定義することで返すことが可能になる
##  ⇒複数種類の変数を乱雑に配置させることなく、必要な値だけ返すことができるようになりそう


def gen_counter():
    """呼び出すごとにカウントを上げるカウンタを生成する"""

    # クロージャ _counter で利用する現在のカウント
    count = 0

    def _counter(reset=False):
          # 関数の外にある count を更新したいので nonlocal 宣言をする
        nonlocal count

        if reset:
            count = 0
        count += 1
        return count

    return _counter

# カウンタを使用する
c1 = gen_counter()

# nonlocal のおかげで更新した count の値が保持できることの確認
print(c1())  # => 1
print(c1())  # => 2
print(c1())  # => 3

print(c1(reset=True))  # => 1
print(c1())  # => 2