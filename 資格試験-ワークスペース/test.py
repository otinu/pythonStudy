import base64
from collections import Counter
from datetime import date, datetime
import enum
import itertools
import math
from pathlib import Path
import re
import sys
import tempfile
from typing import Literal, Union
import unicodedata
from urllib import parse
from xmlrpc.client import DateTime
from operator import itemgetter

from class_sample import User
from class_sample2 import User2


def all_show(user):
    print(user.name)
    print(user.age)
    print(user.address)


def test_return() -> str:
    return "Hello Python"


user1: User = User("おちぬ", "55", "兵庫県姫路市")
user2 = User2("gure")

tmp: str = test_return()

hobby: tuple[str, int] = ("ゲーム", 3)

price: Literal[1000, 2000, 3000] = 1000
price = 2000

test = "World"
print("Hello %s" % test)
print(f"Hello {test}")

now = datetime.now()
f"{now:%Y-%m-%d}"
f"{now:%Y/%m/%d}"
f"{now:%Y年%m月%d}"

print(now.strftime("%y-%m-%d %H:%M:%S"))

print(unicodedata.name("🍺"))
print(unicodedata.lookup("BEER MUG"))

print(unicodedata.normalize("NFKC", "ＫＯＫＯがﾀｲｼｮｳﾓｼﾞﾚﾂです"))
print("ＫＯＫＯがﾀｲｼｮｳﾓｼﾞﾚﾂです")

ganjitsu = date(2021, 1, 1)
print(ganjitsu.strftime("%Y年%m月%d日"))

sorted(["spam", "ham", "pes"])
sorted([2, 29, 10.1])


print(sorted({"a": 1, "c": 2, "b": 3}.items()))

print(sorted("Hello World"))


seq = [0, 4, 1, 2, 3, 5]
rev_seq = reversed(seq)
print(rev_seq)
print(list(rev_seq))


seq_str = ["B", "D", "a", "c"]
print(sorted(seq_str))
print(sorted(seq_str, key=str.lower))

data = [(1, 40, 200), (3, 10, 100), (2, 20, 300), (1, 30, 300)]
print(sorted(data))
print(sorted(data, key=itemgetter(2)))
print(sorted(data, key=itemgetter(2, 0)))

c = Counter(a=4, b=1, c=-2, d=2)
c2 = Counter(a=1, b=3, e=1)
c.subtract(c2)
print(c)
c.update(c2)
print(c)


results = itertools.combinations("ABC", 2)
print([r[0] + r[1] for r in results])

tmp1 = Path("usr", "tmp", "test.txt")
print(tmp1)
tmp1 = Path("/usr", "tmp", "test.txt")
print(tmp1)
print(tmp1.drive)
print(tmp1.anchor)
print(tmp1.parent)
print(tmp1.parents)

print(tmp1.is_relative_to("/usr"))
print(tmp1.is_relative_to("/usr/tmp"))
print(tmp1.is_relative_to("/tmp"))


tmpf = tempfile.NamedTemporaryFile(delete=False)
print(tmpf.name)
p = Path(tmpf.name)
print(p.exists())
tmpf.close()

print(parse.quote("_.-~"))

s = "Python は簡単に習得でき、それでいて強力な言語の1つです。"
enc_s = base64.b64encode(s.encode())
print(base64.b64decode(enc_s).decode())


print([r[0] + r[1] for r in itertools.permutations("ABC", 2)])

print(sys.version_info)


m = re.match(r"(\d+)-(\d+)-(\d+)", "080-1234-5678")
print(m.group())
