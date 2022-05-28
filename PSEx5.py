""" pipの使い方(Pythonチュートリアル)

# pipとはパッケージ管理用のツール ⇒ RubyのGemのようなもの

#パッケージのインストール方法
python -m pip install [パッケージ名]
python -m pip install [パッケージ名①] [パッケージ名②]    #複数インストール
python -m pip install [パッケージ名]==3.9.7                #バージョン指定
python -m pip install --upgrade [パッケージ名]             #アップデート

#パッケージ情報の確認
pip show requests

#インストール済みパッケージの一覧表示
pip list
    【出力】: [パッケージ名](3.9.7)

pip freeze > pacage_list.txt            # freezeは別ファイルに一覧としてまとめておくのが一般的
    【出力】: [パッケージ名]==3.9.7

#パッケージのアンインストール方法

python -m pip uninstall [パッケージ名]
python -m pip uninstall [パッケージ名①] [パッケージ名②]    #複数アンインストール
"""