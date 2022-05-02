#要素番号が奇数のものだけ取り出し
list1 = [1, 2, 3, 4, 5, 6]
print(list1[::2])

#要素番号が偶数のものだけ取り出し
print(list1[1::2])

#逆順に取り出し
print(list1[::-1])

#2次元リスト
first_list = [10, 20, 30]
second_list = [40, 50, 60]
two_dimensional_list = [first_list, second_list]
print(two_dimensional_list)

#リストの末尾に要素を追加(PUSH)
list1.append(100)
print(list1)

#リストの任意の位置に要素を挿入
list1.insert(0, 500)
print(list1)

#リストの末尾を切り取り(POP)
list1.pop()
print(list1)

#リストの任意の位置の要素を切り取り
list1.pop(0)
print(list1)

# +を使うことで、1つの1次元配列として連結もできる
coalescent_list = first_list + second_list;
print(coalescent_list)
