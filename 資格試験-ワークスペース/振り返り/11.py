from pathlib import Path, PurePath

pure = PurePath("pathlib.txt")
path = Path("pathlib.txt")

print(pure)
print(path)

# 純粋パスはI/O機能がないから、物理的なファイルに書き込めない
# pure.write_text("World", encoding="utf-8")

# こっちはエラーにならない
path.write_text("World", encoding="utf-8")
print(path.read_text(encoding="utf-8"))

# 実際にファイルが削除される
# path.unlink()
# print(path.exists())
