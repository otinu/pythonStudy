# round()=============================================
round_data = 0.1414210356
### 第二引数が0のときは、小数点第一位が0になるため注意
print(round(round_data, 2))
print(round(round_data + 1, 0))

# zip()===============================================

zip_data = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
]
print(zip_data)
# ⇒[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
print(list(zip(*zip_data)))
# ⇒[('A', 'D', 'G'), ('B', 'E', 'H'), ('C', 'F', 'I')]