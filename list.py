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