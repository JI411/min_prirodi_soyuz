import os

def delete(SITE):
    print('PATH: /system/delete/dlete.py')

    SOURCE_DIR = 'files/source'
    TIGER_DIR = 'files/result/tiger'
    LEOPARD_DIR = 'files/result/leopard'
    OD_SOURCE_DIR = 'files/object_detection_source'
    OD_PRINCESS_TIGER_DIR = 'files/object_detection_result/tiger'
    OD_PRINCESS_PRINCESS_DIR = 'files/object_detection_result/princess'
    OD_PRINCESS_LEOPARD_DIR = 'files/object_detection_result/leopard'

    dir_list = [
      SOURCE_DIR,
      TIGER_DIR, 
      LEOPARD_DIR, 
      OD_SOURCE_DIR,
      OD_PRINCESS_TIGER_DIR, 
      OD_PRINCESS_PRINCESS_DIR,
      OD_PRINCESS_LEOPARD_DIR
    ]

    for current_dir in dir_list:
        for file_name in os.listdir(current_dir):
            path = f'{current_dir}/{file_name}'
            if os.path.isfile(path):
              os.remove(path)

    SITE.content = '\x1f        <h1>Все файлы удалены</h1>\x1f    '
