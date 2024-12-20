# Теория множеств и булева алгебра
Левахин Лев 343730 К3140  
Практический поток 4.4  
Вариант 2

---

## Описание задачи
Написать программу, которая выводит булеан n-ого порядка заданного множества чисел

## Общие критерии
1. [x] Программа должна быть написана на одном из top-50 языков индекса tiobe
2. [x] Программа должна запускаться на операционных системах UNIX-семейства
3. [x] Программа должна запускаться без взаимодействия с автором программы (допустима инструкция)
4. [x] Программы должны использовать только встроенные в язык библиотеки (нет, numpy и им подобные неразрешены)
> Нарушение хотя бы одного из пунктов ведет к невозможности получить за задание более 0 баллов

## Инструкция по запуску
1. Весь функционал реализован в классе `GenerateBoolean`, который принимает на вход множество.  
Чтобы создать булеан, нужно создать экземпляр этого класса:  
`bolean = GenerateBolean(plenty)`  
После создания булеана, на основе этого класса, следует просто вывести его, т.е **запустить файл:**
```bash
python boolean.py
```
2. Можно задать множество 2 способами:
- В Python файле `boolean.py` изменить `plenty = {1, 2, 3}`
- В файле `input.txt`

3. Во втором случае следует записать нужные значения в файл `input.txt` **каждое с новой строки(как в примере)** и запустить файл
`generate_bolean_from_input_file.py`
```bash
python generate_boolean_from_input_file.py
```
