"""
【17:デバッグ】
次のコードを実行後、pdbでnumの値を確認するには、どの順番でコマンドを叩けばいいか
1.n
2.p num
※nはnextのことで、現在行から次の行に進む
"""
import sys


def get_system_implementation():
    result = sys.implementation
    # ブレークポイントを挿入する
    breakpoint()
    num = 1 + 2
    return result


def main():
    get_system_implementation()


if __name__ == "__main__":
    main()
