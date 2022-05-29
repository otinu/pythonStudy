# ifの末尾に「:」が入らない点に注意
result = [n for n in range(10) if n % 2 == 0]
print(result)
# ⇒ [0, 2, 4, 6, 8]

# 辞書型をループするとき、ブロック変数の中には各キーが入っている点に注意
fishs = {"tinu": "黒鯛", "gure": "クロ", "bera": "キュウセン"}
for fish in fishs:
    print(fishs[fish], end="")
    # ⇒ 黒鯛クロキュウセン

for fish in fishs.values():
    print(fishs[fish], end="")
# ⇒ 黒鯛クロキュウセン

#下記のように、複数の代入を一度に実行する処理を【多重代入】という
tajyu1, tajyu2 = 1, 2