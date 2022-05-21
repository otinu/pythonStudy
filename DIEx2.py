import json #☆①

# ファイル操作==================================================

"""
①r: 読み込み
②w: 書き込み
③r+, w+: 読み書き
④a+: 読み書きモードで新規作成orファイルを開く
⑤x+:  指定するファイル名が存在しなければ、新規作成
"""
path = "test.txt"
f = open(path)
###文字コードの指定も可能
with open(path, 'r', encoding='UTF-8') as f:
    s = f.read()
    print(type(s))
    print(s)

# JSON=========================================================
# Decimalはインポートが必要 ☆①

### JSONに変換
### ⇒この場合、キーとバリュー(文字列の場合)の値がシングルからダブルクオートで囲われるようになる
json_data = {'name':'yamada','data':[2,3,4]}
print(json.dumps(json_data))

# 呼び出しのタイミングと変数・引数=============================

## 1回目は引数なしでnumを呼び出し
    #既存の変数iの値は10であり、これをargに代入
i = 10
def num(arg=i):
    print(arg)
print("1回目===")
num()

i = 7
## 2回目呼び出し時点ではiの値は7に置き換わっている
    # num()の『定義直前までのiの値』が使われている
print("2回目===")
num()
## 3回目呼び出しでは『呼び出し直前までのiの値』が使われている
print("3回目===")
num(i)

# ラムダ(sort)==============================================

## sort() + x[2:] で、「要素番号0から2要素ずつループ」
lst = ['id01', 'id10', 'id02', 'id12', 'id03', 'id13']
lst_sorted = sorted(lst, key=lambda x: int(x[2:]))
print(lst_sorted)

## sort() + x[1]で、「各要素の要素番号1を基にループ」
## ⇒バリューを昇順にソートする
lst = [('Mark',1),('Jack',5),('Jake',7),('Sam',3)]
lst_sorted = sorted(lst, key=lambda x: x[1])
print(lst_sorted)

## オブジェクトの好みのフィールドでソートする
dic = [(1, 'Noro'), (2, 'Nakao'), (3, 'Miyaoka'), (4, 'Kimura')]
dic.sort(key=lambda dic: dic[1])
print(dic)

birthday_list = [
    {
        'name': 'Taro',
        'city': 'Tokyo',
        'birthday': 19990303
    },
    {
        'name': 'Hanako',
        'city': 'Osaka',
       'birthday': 19990301
    },
    {
        'name': 'Jiro',
        'city': 'Fukuoka',
        'birthday': 19990302

}]
lam = sorted(birthday_list, key=lambda x: x['birthday'])
print("お誕生日順に並んでください")
print(lam)