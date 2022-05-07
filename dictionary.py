#dictionary(連想配列)型
d = {"a": 100, "b": 200}
print(d["a"])

#要素の置き換え
d["a"] = 1
print(d["a"])

#要素の追加
d["c"] = 300
print(d)

'''
# キーをクオテーションで囲わないのはNG
d2 = {x: 1000, y: 2000}
print(d2[x])
'''
