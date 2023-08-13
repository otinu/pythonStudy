# 【6:テキストの処理】？
import datetime
from datetime import date, time


t = datetime.datetime(2021, 2, 14, 17, 26, 8, 585404)
# これはいける
print(f"{t:%Y年}{t:%m月}")
print(f"{t:%Y年%m月}")

# これもいける
date = datetime.date(2023, 1, 1)
time = datetime.time(0, 0, 0)
print(f"{date:%Y/%m/%d} {time:%H:%M:%S}")

# これはエラー
# print(f"{t.year:%Y年}")　# 👈t.yearやt.monthとなるとアウト。
# print(f"{t.year:%Y年}{t.month:}")
