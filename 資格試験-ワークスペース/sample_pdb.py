def div(a, b):
    return a / b


def main():
    # 以下を実行すると 1 / 0 でZeroDivisionErrorが発生する
    div(1, 0)


if __name__ == "__main__":
    main()
