# Теория множеств и булева алгебра
Левахин Лев 343730 К3140  
Практический поток 4.4  
Вариант 2

---

## Описание задачи
Написать программу, которая строит дерево Хаффмана и коды Хаффмана для произвольного текста

## Общие критерии
1. [x] Программа должна быть написана на одном из top-50 языков индекса tiobe
2. [x] Программа должна запускаться на операционных системах UNIX-семейства
3. [x] Программа должна запускаться без взаимодействия с автором программы (допустима инструкция)
4. [x] Программы должны использовать только встроенные в язык библиотеки (нет, numpy и им подобные неразрешены)
> Нарушение хотя бы одного из пунктов ведет к невозможности получить за задание более 0 баллов

## Инструкция по запуску
1. Весь функционал реализован в классе ``, который принимает на вход строку.  
Чтобы запустить программу, нужно создать экземпляр этого класса:  
``  
После создания объекта, на основе этого класса, следует просто вывести его, т.е **запустить файл:**
```bash
python huffman.py
```
2. Можно задать строку 2 способами:
- В Python файле `huffman.py` изменить `text = ""`
- В файле `input.txt`

3. Во втором случае следует записать текст в файл `input.txt` как в примере и запустить файл
`generate_huffman_from_input_file.py`
```bash
python generate_huffman_from_input_file.py
```