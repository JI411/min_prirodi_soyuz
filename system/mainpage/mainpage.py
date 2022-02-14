from datetime import datetime

def mainpage(SITE):
    current_datetime = datetime.now()
    print(current_datetime)
    print('/system/mainpage/mainpage.py')

    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')
    SITE.addHeadFile('/templates/system/css/mainpage.css')
    SITE.addHeadFile('/templates/system/js/process.js')

    SITE.content = '\x1f        <h1>Загрузить файлы</h1>\x1f        <div class="mainpage_warning">Возможна загрузка нескольких изображений одновременно. Выберите несколько изображений.</div>\x1f        <div class="dan_flex_row_start mainpage_input_container">\x1f            <div class="mainpage_desc_input">Формат ".jpg",<br>размер - от 640 пикселей (оптимальный).</div>\x1f            <div><input id="mainpage_files" type="file" multiple="multiple" name="files[]"></div>\x1f        </div>\x1f        <div class="mainpage_pt_20"><input id="mainpage_submit" class="dan_button_green" type="button" value="Отправить"></div>\x1f    '
