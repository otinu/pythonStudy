class User:  # Userというクラスを定義
    user_type = None  # データ属性としてuser_typeを初期値Noneで宣言

    def __init__(self, name, age, address):  # コンストラクターメソッド
        self.name = name  # インスタンス変数name、age、addressにコンストラクター引数の値を代入
        self.age = age
        self.address = address

    def increment_age(self):
        """年齢を1つ増やす"""
        self.age += 1

    def start_name(self):
        """nameの1文字目を取得する"""
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ""

    def __repr__(self):
        return f"<User id:{id(self)} name:{self.name}>"

    def __len__(self):
        return len(self.name)
