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