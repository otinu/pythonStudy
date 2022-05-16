"""
#Pleiadesでのサードパーティライブラリ利用方法

【前提条件】
Pleiadesで実行するpython.exeはpleiades配下にないといけない

【手順】
①get-pip.pyをDLして、Pleiades配下のpython.exeと同じ配下に保存
②cmdを起動し、①の配下に移動した後「.\python.exe .\get-pip.py」を実行
③Pleiadesにて、「ウインドウ」>「設定」>「Pydev」>「Pythonインタプリタ」を開く
④「pipで管理」より、「install 〇〇」を実行
⑤ ④でインストール後、下記のように利用するファイルでインポート
"""

from termcolor import colored
print(colored("Hello", "green", "on_yellow" ))