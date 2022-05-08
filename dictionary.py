#dictionary(連想配列)型
d = {"a": 100, "b": 200}
print(d["a"])

#要素の置き換え
d["a"] = 1
print(d["a"])
d["a"] = 100

#要素の追加
d["c"] = 300
print(d)

'''
# キーをクオテーションで囲わないのはNG
d2 = {x: 1000, y: 2000}
print(d2[x])
'''
d3 = {"d": 400, "e": 500, "f": 600}

#コピー
print(d3.get("d"))

#配列の中身をリセット
d3.clear()
print(d3)

#ある配列に別の配列を上書き
d3.update(d)
print(d3)

#指定したキーが配列内にあるか判定
print("e" in d3)
print("b" in d3)