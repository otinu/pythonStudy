# set型(集合)は重複を除いて表示される
a = {1, 2, 2, 3, 3, 4, 5, 5}
print(a)
print(type(a))

b = {2, 3, 5, 6, 7}

# 集合の差や積などを求めることもできる
print(a - b)
print(a & b)

b.add(8)
print(b)