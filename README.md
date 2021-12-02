# Tiger & Leopards & Princess Detection in The Wild
Создано командой "Союз" во время участия в [хакатоне](https://hacks-ai.ru/hakaton/samara).
* Фронтенд решение реализован на фреймворке aiohttp с шаблонизатором jinja
* Скрипт по обработке модели находится в папке /system/ajax/ajax.py код классификации изображений на основе предобученной модели efficientNetB7
* Скрипт обнаружения принцессы находится в папке /object_detection в полном решнии (ссылка ниже)
* Модели находятся в папке /files/model в полном решнии (ссылка ниже)
* [Скрипт](/PREDICT.ipynb) расчета по первой задаче 
* [Демонстрация](https://colab.research.google.com/github/JI411/min_prirodi_soyuz/blob/main/princess.ipynb) отделения Принцессы от остальных тигров (yolov5)
* В корне находятся лейблы классификации на тестовых данных (тигры, леопарды, прочее): labels.csv, принцесса: labels_princess.csv
* **Полное решение** с моделями и весами находится на диске https://drive.google.com/file/d/1uCQ0MOPU5-I6GG39xrmk4KQk8bskinLn/view?usp=sharing
