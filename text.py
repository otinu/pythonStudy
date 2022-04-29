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

#formatメソッドを使って、文字列内への代入が可能
set_word = "1番は{}, 2番は{}, 3番は{} が正解でした".format("イ", "ウ", "ア")
print(set_word)

set2_word = "1番は{2}, 2番は{0}, 3番は{1} が正解でした".format("イ", "ウ", "ア") #代入の順番を変更
print(set2_word)

set3_word = "昨日は{reading}して、今日は{fishing}をしました".format(reading = "読書", fishing = "釣り")
print(set3_word)

#print()内の引数に「f + 文字列」を使うことで、文字列型の変数を直接代入可能
reading = "読書"
fishing = "釣り"
print(f"キャンプでは{reading}と{fishing}をしよう")
