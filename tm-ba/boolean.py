"""Написать программу, которая выводит булеан n-ого порядка заданного множества чисел"""

from itertools import product


class GenerateBoolean:
    """
    Поиск булеана n-ого порядка
     Булеан - множество всех подмножеств
    """

    def __init__(self, plenty:set):
        self.plenty = list(plenty)
        self.capacity = len(plenty)

        self.boolean = self.generate_boolean_array()

    def __str__(self):
        result = "{"
        for array in self.boolean:
            result += "{" + ", ".join(array) + "}" + ", "
        result = result[:-2]
        result += "}"

        return result

    def generate_boolean_array(self):
        """Генерирует булеан n-ого порядка"""

        # Генерируем все возможные комбинации истинных и ложных значений для мощности множества
        bool_combinations = list(product([False, True], repeat=self.capacity))

        # Преобразуем каждую комбинацию(тру или фолз) в список, состоящий из элементов исходного множества(где тру, ставим элемент множества, где фолз - ничего)
        result = []
        for combination in bool_combinations:
            boolean_element = []
            for i, value in enumerate(combination):
                if value:
                    boolean_element.append(str(self.plenty[i]))
            result.append(boolean_element)

        return result


if __name__ == "__main__":
    plenty = {1, 2, 3, 45}
    boolean = GenerateBoolean(plenty)
    print(boolean)