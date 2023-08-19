import requests  # 「pip install requests」などが必要

# GETメソッド
r = requests.get("http://httpbin.org/get", params="example")
# print(dir(r))
print(r.url)
print(r.text)
print(r.headers)
print(r.url)

# ヘッダー指定
headers = {"Accept": "application/json"}
r = requests.get("http://httpbin.org/get", headers=headers)
print(r.json())  # jsonは属性ではなく、メソッドとして呼び出す

# POSTメソッド
payload = {"hoge": "fuga"}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.request.body)

# SSL証明書の確認を無効にする
# 　⇒社内の開発環境でのエラーを避けるためなど
r = requests.get("http://httpbin.org/get", verify=False)

# 文字コードを自動判別
r.encoding = r.apparent_encoding
print(r.text)

"""
# requestのほうが少し早い？
from urllib import request
r = requests.get("http://httpbin.org/get")
"""
