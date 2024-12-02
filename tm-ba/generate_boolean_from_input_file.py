"""Выводит булеан на основе файла input.txt"""

from boolean import GenerateBoolean


def utils() -> list:
    """Считывает данные из файла input.txt в множество"""
    plenty = []

    with open("input.txt", "r") as file:
        for s in file:
            element = s.strip()
            if element not in plenty:
                plenty.append(element)

    return plenty

def display():
    boolean = GenerateBoolean(utils())
    print(f"Множество, которое вы ввели: {utils()}")
    print(f"Булеан этого множества: {boolean}")


if __name__ == "__main__":
    display()
