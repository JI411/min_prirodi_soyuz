import os
from datetime import datetime

def result(SITE):
    print('PATH: /system/result/result.py')

    TIGER_DIR = 'files/result/tiger/'
    LEOPARD_DIR = 'files/result/leopard/'

    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')
    SITE.addHeadFile('/templates/system/css/result.css')
    SITE.addHeadFile('/templates/system/js/result.js')

    tigers_html = ''
    for file_name in sorted(os.listdir(TIGER_DIR)):
        name = file_name if len(file_name) < 20 else file_name[:20] + '...'
        tigers_html +=  '<div class="item_wrap">'
        tigers_html +=      '<img class="item_image" src="/files/result/tiger/' + file_name + '">'
        tigers_html +=      '<div class="item_name">' + name + '</div>'
        tigers_html +=  '</div>'

    leopards_html = ''
    for file_name in sorted(os.listdir(LEOPARD_DIR)):
        name = file_name if len(file_name) < 20 else file_name[:20] + '...'
        leopards_html +=  '<div class="item_wrap">'
        leopards_html +=      '<img class="item_image" src="/files/result/leopard/' + file_name + '">'
        leopards_html +=      '<div class="item_name">' + name + '</div>'
        leopards_html +=  '</div>'

    SITE.content = f'''
        <h1>Результат</h1>
        <h2>Тигры</h2>
        <div id="tigers_container" class="dan_flex_row_start">{tigers_html}</div>
        <div class="result_separator"></div>
        <h2>Леопарды</h2>
        <div id="leopards_container" class="dan_flex_row_start">{leopards_html}</div>
    '''
