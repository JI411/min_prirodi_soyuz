import os
import shutil
import numpy as np
import json
from datetime import datetime

import torch


# Загрузка файла
def object_detection_upload_ajax(SITE):
    print('PATH: /system/object_detection_ajax.py -> object_detection_upload_ajax')
    current_datetime = datetime.now()
    print(current_datetime)

    image_file = SITE.post['image'].file.read()
    image_file_name = SITE.post['image'].filename.lower()

    # Сохраняем 'jpg' файл
    with open('files/object_detection_source/' + image_file_name, 'wb') as f:
        f.write(image_file)

    # Выделяем имя файла
    name = image_file_name.split('.')[0]

    answer = {'answer': 'success', 'name': name}
    return {'ajax': json.dumps(answer)}


# Обработка файлов
def object_detection_processing_ajax(SITE):
    print('PATH: /system/object_detection_ajax.py -> object_detection_processing_ajax')

    SOURCE_DIR = 'files/object_detection_source'
    TIGER_DIR = 'files/object_detection_result/tiger'
    PRINCESS_DIR = 'files/object_detection_result/princess'
    LEOPARD_DIR = 'files/object_detection_result/leopard'
    IMG_SIZE = 640
    TRESHOLD = 0.5

    if 'treshold' in SITE.post and float(SITE.post['treshold']) >= 0.05 and float(SITE.post['treshold']) <= 0.7:
      TRESHOLD = float(SITE.post['treshold'])

    # Загружаем модель
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='files/model/yolo_640.pt')
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.multi_label = True  # NMS multiple labels per box
    model.max_det = 10  # maximum number of detections per image


    for file_name in sorted(os.listdir(SOURCE_DIR)): 
        results = model(SOURCE_DIR + '/' + file_name)

        print('================== Успешно! ========================')
        results.print()

        labels, cord_thres = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy()

        if labels:
            print('Класс:', labels[0])

            if labels[0] == 0:
                results.save(TIGER_DIR)
            
            if labels[0] == 1:
                results.save(LEOPARD_DIR)

            if labels[0] == 2:
                results.save(PRINCESS_DIR)

    object_detection_source_delete(SITE)  # Удаляем файлы из папки source

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}


# Удаление элементов
def object_detection_source_delete(SITE):
    SOURCE_DIR = 'files/object_detection_source'

    for file_name in os.listdir(SOURCE_DIR):
        path = SOURCE_DIR + '/' + file_name
        if os.path.isfile(path):
            os.remove(path)

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}








