"""Генерирует дерево и коды Хаффмана на основе текста из файла инпут"""

from huffman import GenerateHuffman


def utils() -> str:
    """Считывает данные из файла input.txt в множество"""
    text = []
    with open("input.txt", "r", encoding="utf8") as file:
        for s in file:
            text.append(s.strip())

    result = " ".join(text)

    return result

def display():
    """Выводит коды и дерево Хаффмана"""
    print(f"Вот текст, который вы ввели: {utils()}")
    huffman = GenerateHuffman(utils())
    huffman.display_huffman_codes()
    huffman.display_huffman_tree()


if __name__ == "__main__":
    display()