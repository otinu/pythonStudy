num = 1
name = "tinu"

# numの型を確認
print(num, type(num))

# 代入される値によって、型は動的に変動
num = name
print(num, type(num))

name = "2022"
new_name = int(name)
print(new_name, type(new_name))