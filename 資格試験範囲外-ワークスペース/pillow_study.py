from PIL import Image, ImageDraw, ImageFont

# 画像の読み込み
img = Image.open("lockon_dog.png")
# 200px x 200pxにリサイズ

# thumbnail()の特徴
# 1.元の画像サイズを大きくすることはない
# 2.指定された範囲内で最大サイズに調節する
size = (200, 200)
img.thumbnail(size)

# 反時計回りに90度回転
rotated_img = img.rotate(90)

# 書き込み用のインスタンス作成
draw = ImageDraw.Draw(rotated_img)

# フォントの指定
# C:\Windows\Fonts にフォント用ファイルは置かれている
font = ImageFont.truetype("UDDIGIKYOKASHON-B.TTC", 24)

# テキストの埋め込み
draw.text((35, 30), "No Japanese!!", "red", font=font)

rotated_img.save("made_lockon_dog.png", quality=100)
