# 例外処理

l = [1, 2, 3]
i = 5

try:
    l[0]
except IndexError as ex:
    print("IndexError")
except NameError as ex:
    print("NameError")
except Exception as ex:
    print("Exception")
else:
    print("その他")
finally:
    print("Finally")
