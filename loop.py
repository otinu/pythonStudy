count = 0
while True:
        if count >= 5:
            break
        if count == 2:
            count += 1
            continue

        print(count)
        count += 1

print("========")
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print('done')

while True:
    # input()で入力受付
    word = input('Enter:')
    num = int(word) # 受け付ける値は全てStringになるため、変換
    if num == 100:
        break
    print('next')

# ブロック変数の利用
word_list = ["I", "have", "an", "apple"]
for word in word_list:
    print(word)
#文字列は1文字ずつに切り分けて取り出してくれる
for character in "APPLE":
    print(character)

#for-else文の場合、ブロック変数はリストの末尾の要素をもった状態でelseへ移行する
for fruit in ["apple", "banana", "orange"]:
    if fruit == "banana":
        print("I like banana")
        #break
    print(fruit)
else:
    print(fruit + "は別腹")