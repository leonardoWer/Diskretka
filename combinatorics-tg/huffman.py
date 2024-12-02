"""Написать программу, которая строит дерево Хаффмана и коды Хаффмана для произвольного текста"""

import heapq
from collections import defaultdict


class Node:
    """Класс для представления узла дерева Хаффмана"""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Определение порядка для использования в куче"""
        return self.freq < other.freq


class GenerateHuffman:
    """Строит дерево Хаффмана и коды Хаффмана для произвольного текста"""

    def __init__(self, text: str):
        self.text = text
        self.huffman_codes = {}  # Словарь для кодов Хаффмана
        self.huffman_tree = self.build_huffman_tree()  # Создание дерева Хаффмана
        self.generate_codes(self.huffman_tree)  # Генерация кодов Хаффмана

    def build_huffman_tree(self):
        """Создание дерева Хаффмана"""
        # Подсчет частоты каждого символа
        freq = defaultdict(int)
        for char in self.text:
            freq[char] += 1

        # Создание приоритетной очереди (кучи)
        heap = []
        for char, frequency in freq.items():
            heapq.heappush(heap, Node(char, frequency))

        # Построение дерева Хаффмана
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

        return heap[0]  # Корень дерева

    def generate_codes(self, node, current_code=""):
        """Генерирует коды Хаффмана для каждого символа"""
        if node is not None:
            # Если в узле есть символ
            if node.char is not None:
                self.huffman_codes[node.char] = current_code
            # Рекурсивный вызов для левого и правого поддеревьев
            self.generate_codes(node.left, current_code + "0")
            self.generate_codes(node.right, current_code + "1")

    def display_huffman_codes(self):
        """Выводит коды Хаффмана"""
        print("Коды Хаффмана для введённого текста:")
        for char, code in self.huffman_codes.items():
            print(f"{char}: {code}")

    def display_huffman_tree(self):
        """Выводит дерево Хаффмана"""
        print("Дерево Хаффмана для введённого текста:")
        self._display_huffman_tree(self.huffman_tree)

    def _display_huffman_tree(self, node, prefix=""):
        """Вспомогательный метод для рекурсивного вывода дерева Хаффмана"""
        if node is not None:
            if node.char is not None:
                print(f"{prefix} -> {node.char} ({node.freq})")
            else:
                print(f"{prefix} -> * ({node.freq})")  # Узел без символа (внутренний узел)

            # Рекурсивно выводим левое и правое поддеревья
            self._display_huffman_tree(node.left, prefix + "    0")
            self._display_huffman_tree(node.right, prefix + "    1")


if __name__ == "__main__":
    huffman = GenerateHuffman("leva")
    huffman.display_huffman_codes()
    huffman.display_huffman_tree()
