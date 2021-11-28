import os
from datetime import datetime

def object_detection(SITE):
    print('PATH: /system/object_detection/object_detection.py')

    TIGER_DIR = 'files/object_detection_result/tiger/'
    PRINCESS_DIR = 'files/object_detection_result/princess/'
    LEOPARD_DIR = 'files/object_detection_result/leopard/'

    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')
    SITE.addHeadFile('/templates/system/css/mainpage.css')
    SITE.addHeadFile('/templates/system/css/result.css')
    SITE.addHeadFile('/templates/system/js/object_detection.js')

    # Тигры
    tigers_html = ''
    for file_name in sorted(os.listdir(TIGER_DIR)):
        name = file_name if len(file_name) < 20 else file_name[:20] + '...'
        tigers_html +=  '<div class="item_wrap">'
        tigers_html +=      '<img class="item_image" src="/files/object_detection_result/tiger/' + file_name + '">'
        tigers_html +=      '<div class="item_name">' + name + '</div>'
        tigers_html +=  '</div>'

    # Принцесса
    princess_html = ''
    for file_name in sorted(os.listdir(PRINCESS_DIR)):
        name = file_name if len(file_name) < 20 else file_name[:20] + '...'
        princess_html +=  '<div class="item_wrap">'
        princess_html +=      '<img class="item_image" src="/files/object_detection_result/princess/' + file_name + '">'
        princess_html +=      '<div class="item_name">' + name + '</div>'
        princess_html +=  '</div>'

    # Леопарды
    leopards_html = ''
    for file_name in sorted(os.listdir(LEOPARD_DIR)):
        name = file_name if len(file_name) < 20 else file_name[:20] + '...'
        leopards_html +=  '<div class="item_wrap">'
        leopards_html +=      '<img class="item_image" src="/files/object_detection_result/leopard/' + file_name + '">'
        leopards_html +=      '<div class="item_name">' + name + '</div>'
        leopards_html +=  '</div>'

    SITE.content = f'''
        <h1>Обнаружение объектов</h1>
        <div class="mainpage_warning">Возможна загрузка нескольких изображений одновременно. Выберите несколько изображений.</div>
        <div class="dan_flex_row_start mainpage_input_container">
            <div class="mainpage_desc_input">Формат ".jpg",<br>размер - от 640 пикселей (оптимальный).</div>
            <div><input id="mainpage_files" type="file" multiple="multiple" name="files[]"></div>
        </div>
        <div class="mainpage_pt_20"><input id="mainpage_submit" class="dan_button_green" type="button" value="Отправить"></div>
        <h2>Тигры (кроме принцессы)</h2>
        <div id="tigers_container" class="dan_flex_row_start">{tigers_html}</div>
        <div class="object_detection_separator"></div>
        <h2>Принцесса</h2>
        <div id="princess_container" class="dan_flex_row_start">{princess_html}</div>
        <div class="object_detection_separator"></div>
        <h2>Леопарды</h2>
        <div id="leopards_container" class="dan_flex_row_start">{leopards_html}</div>
    '''