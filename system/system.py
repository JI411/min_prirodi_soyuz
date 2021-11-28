from aiohttp import web
from system.mainpage import mainpage
from system.result import result
from system.object_detection import object_detection
from system.object_detection_ajax import object_detection_ajax
from system.delete import delete
from system.ajax import ajax

def router(SITE):
    print('PATH: /system/system.py')

    if SITE.p[1] == 'auth':  # Если заход с формы
        return {'redirect': '/system/'}

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'result': result.result,
        'object_detection': object_detection.object_detection,
        'object_detection_upload_ajax': object_detection_ajax.object_detection_upload_ajax,
        'object_detection_processing_ajax': object_detection_ajax.object_detection_processing_ajax,
        'delete': delete.delete,
        'image_upload_ajax': ajax.image_upload_ajax,
        'image_processing_ajax': ajax.image_processing_ajax,
        'image_source_delete': ajax.image_source_delete,
    }

    if (SITE.p[1] not in functions):
        raise web.HTTPNotFound()

    # Вызов функции из словаря
    return functions[SITE.p[1]](SITE)
