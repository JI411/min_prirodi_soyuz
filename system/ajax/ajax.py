import os
import shutil
import numpy as np
import json
from datetime import datetime

import matplotlib.pyplot as plt

from skimage.io import imread  # Чтение файла сразу в np массив, для варианта с обрезкой

import tensorflow as tf
from tensorflow.keras.preprocessing import image  # Для работы с изображениями 
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB0
from keras.applications.imagenet_utils import decode_predictions  # Для декодирования лейблов
from tensorflow.keras.applications import EfficientNetB7


# Загрузка файла
def image_upload_ajax(SITE):
    current_datetime = datetime.now()
    print(current_datetime)
    print('PATH: /system/ajax.py -> image_upload_ajax')

    image_file = SITE.post['image'].file.read()
    image_file_name = SITE.post['image'].filename.lower()

    # Сохраняем 'jpg' файл
    with open(f'files/source/{image_file_name}', 'wb') as f:
        f.write(image_file)

    # Выделяем имя файла
    name = image_file_name.split('.')[0]

    answer = {'answer': 'success', 'name': name}
    return {'ajax': json.dumps(answer)}


# Обработка файлов
def image_processing_ajax(SITE):
    SOURCE_DIR = 'files/source/'
    TIGER_DIR = 'files/result/tiger/'
    LEOPARD_DIR = 'files/result/leopard/'
    IMG_SIZE = 600
    TRESHOLD = 0.05

    if 'treshold' in SITE.post and float(SITE.post['treshold']) >= 0.05 and float(SITE.post['treshold']) <= 0.7:
      TRESHOLD = float(SITE.post['treshold'])

    # Загружаем модель - стало только хуже. РАЗОБРАТЬСЯ!!!
    # model = tf.keras.models.load_model('files/model/model_e.h5')
    # Пока этот вариант!
    model = EfficientNetB7(weights='imagenet')

    data_list = []
    name_list = []

    for file_name in sorted(os.listdir(SOURCE_DIR)): 
      img = image.load_img(
        path = os.path.join(SOURCE_DIR , file_name), 
        color_mode='rgb', 
        target_size=(IMG_SIZE, IMG_SIZE),
      )
      np_img = image.img_to_array(img)
      data_list.append(np_img)
      name_list.append(file_name)

    x_data = np.array(data_list)
    print('X DATA SHAPE:', x_data.shape)

    y = model.predict(x_data)
    predict = decode_predictions(y)

    predict_list = []
    for i, pred in enumerate(predict):  # Проходим по изображениям
        result_list = []
        for p in pred:  # Проходим по предсказаниям изображения (по умолчанию 5)
          source_path = SOURCE_DIR + name_list[i]
          if p[1] == 'tiger' and p[2] > TRESHOLD:
            result_path = TIGER_DIR + name_list[i]
            shutil.move(source_path, result_path)
            result_list.append('Тигр')
            print(name_list[i], 'Тигр')
          if p[1] == 'leopard' and p[2] > TRESHOLD:
            result_path = LEOPARD_DIR + name_list[i]
            shutil.move(source_path, result_path)
            result_list.append('Леопард')
            print(name_list[i], 'Леопард')
        predict_list.append(", ".join(result_list))
    image_source_delete(SITE)  # Удаляем файлы из папки source

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}


# Удаление элементов
def image_source_delete(SITE):
    SOURCE_DIR = 'files/source'

    for file_name in os.listdir(SOURCE_DIR):
        path = f'{SOURCE_DIR}/{file_name}'
        if os.path.isfile(path):
          os.remove(path)

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}