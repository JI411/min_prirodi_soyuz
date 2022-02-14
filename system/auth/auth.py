import time
from datetime import datetime

def auth(SITE):
    current_datetime = datetime.now()
    print(current_datetime)
    print('AUTH')

    if (SITE.p[1] == 'auth'):
        if (SITE.request.method == 'POST'):
            print('Проверка пароля', SITE.post)
            if ('login' in SITE.post and 
                'password' in SITE.post and
                'button' in SITE.post and
                SITE.post['login'] == 'admin' and 
                SITE.post['password'] == 'test1234'):

                print('Проверка пароля прошла успешно!')

                SITE.session['auth'] = time.time()
            else:
                print('Проверка пароля прошла НЕ успешно!')
        return {'redirect': '/system/'}
    # Авторизация для администратора
    if SITE.auth == 1:
        return

    # Нет авторизации - выводим фому
    if SITE.auth == 0:
        SITE.addHeadFile('/lib/DAN/DAN.css')
        SITE.addHeadFile('/templates/system/css/login.css')

        SITE.title = 'Авторизация'
        SITE.content = '''<form method="post" action="/system/auth">
        <div class="login_form_container">
            <div class="login_form_text">Логин (admin)</div>
            <div><input name="login" class="dan_input" value="admin"></div>
            <div class="login_form_text">Пароль</div>
            <div><input name="password" class="dan_input" type="password" value=""></div>
            <div><input name="button" class="dan_input login_form_submit" type="submit" value="Вход"></div>
        </div>
        </form>
        '''
