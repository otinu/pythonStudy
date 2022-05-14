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