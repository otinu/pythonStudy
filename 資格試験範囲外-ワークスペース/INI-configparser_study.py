from configparser import ConfigParser

# INIファイルの読み込み
config = ConfigParser()
config.read("config.ini")

# セクションの一覧取得(DEFAULもごちゃまぜ)
print(config.sections())

# 特定オプションの一覧を取得する
print(config.options("Tinu"))

print("Tinu" in config)  # セクションの存在確認
print(config["Tinu"]["group"])  # オプションの値を取得
print(config["Tinu"]["Limit"])  # DEFAULT値の採用

# 自分とDEFAULTで重複したら、自分のオプションを優先
print(config["Tinu"]["home_dir"])

# 自分にもDEFAULTにもないものを指定するとエラーになる
# config["Tinu"]["Limit"]

# INIファイル側で%(変数)s とすると、オプション内で展開ができる
print(config["Tinu"]["work_dir"])
