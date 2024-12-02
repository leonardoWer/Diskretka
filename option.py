"""Расчёт варианта"""


def find_option() -> int:
    isu = 3434730
    my_option = isu**isu % 7 + 1
    return my_option


if __name__ == "__main__":
    print(find_option())