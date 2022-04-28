from lxml.html.diff import is_start_tag

word = "python"
print(word[0]) # 0が先頭
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[-1]) # -1が末尾

# ダブルコロンで区切って範囲選択も可能(n:m)
#　⇒n～m-1 を抽出
print(word[0:2])
print(word[2:5])

# 範囲選択で片方を省略可能
print(word[:2])
print(word[2:])

# 文字列の一部だけを置換するのは大変
# 何かしたインポートすれば、容易に解決できる気がする
word = "j" + word[1:]
print(word)

string = "Hello World"
is_start = string.startswith("Hell")
print(is_start)