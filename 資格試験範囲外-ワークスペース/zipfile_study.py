import zipfile

file_name = "ziptest.zip"
if zipfile.is_zipfile(file_name):
    zip = zipfile.ZipFile(file_name)

# zip内のファイル名一覧
print(zip.namelist())

# zip内のファイル数
print(len(zip.namelist()))

name = ""
with zip.open(zip.namelist()[0]) as f:
    print(f.read().decode())  # 日本語を含むならデコード

# zip内ファイルの詳細情報を取得
first_file = zip.getinfo("ziptest.txt")
print(dir(first_file))
print(first_file.date_time)
print(first_file.filename)

# 対象ファイルを選択して、zipファイルを作成
with zipfile.ZipFile("example.zip", mode="w") as wzip:
    wzip.write("zip_add.txt")
    wzip.write("zip_add2.txt")
    wzip.write("zip-追加.txt")

# zip内のファイル名に日本語が含まれていると文字化けする
for name in zip.namelist():
    # 下記のように記述して問題解消
    print(name.encode("cp437").decode("utf-8", "ignore"))

print("------")
# コード上で作成したzip内なら日本語ファイルが含まれてもデコード不要
for name in wzip.namelist():
    print(name)
