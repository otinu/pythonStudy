
#pythonのif文では()を使わず、インデントで識別する
#インデントは半角空白4回(Tabキー2回)分空けるのが暗黙の了解

x = 5
if x < 0:
    print('Hello')
elif x == 0:
    print("〇〇")
else:
    print('Python')

#細かいif文が連続する場合、{}を使わないため注意が必要
# ⇒昔のJavaの書き方と同じ
if x == 100:
    print("△")
if x == 200:
    print("✕")