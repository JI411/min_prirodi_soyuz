from aiohttp import web
import sys
# sys.path.append('index/mainpage')
# sys.path.append('index/page')


def router(SITE):
    # Вызов функций по ключу
    functions = {
        # '': mainpage.mainpage,
        # 'page': page.page,
    }

    if (SITE.p[0] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[0]](SITE)

