#Тестовое задание в NeutoNet 

## структура решения

### general.py

В general.py реализован объект VoiceService, который композирует основые 
интерфейсы библиотеки NeuroNetLibrary. в нём реализовано 2 метода:
* synth_and_recognize
* loop_synth_and_recognize 

#### Метод synth_and_recognize
 Использует 2 метода из NeuroVoiceLibrary 
 nv.synthesize(text, ssml: True|False)  и nv.listen()
 запускает синтез, разспонование и выделения сущностей.
 Если распознование было успешно, возращается объект recognition_result -
 результат выполнения nv.listen()

### Метод loop_synth_and_recognize
Предназначен для синтеза, разспонование и выделения сущностей N раз, 
пока не будет получен  recognition_result

## phrases.py
Словарь фраз

## actions.py
Реализация actions

## main.py
Реализация базовой логики опроса

## hello.py
Реализация логики приветствия

