from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .forms import LoginForm


def user_login(request):
    # проверяем пост запрос, if request 'post'
    if request.method == 'POST':
        # создаем экземпляр формы с данным из post запроса
        form = LoginForm(request.POST)
        # проверяем валидность формы,  если не валидна в шаблоне отображаются ошибки формы
        if form.is_valid():
            # с помощью метода cleaned_data забираем данные из формы
            cln_data = form.cleaned_data
            # метод authenticate() проверяет данные в БД и возвращает нам объект User
            user = authenticate(username=cln_data['username'], password=cln_data['passwords'])
            # проверяем есть ли указнные пользователь
            if user is not None:
                # проверяем активен ли пользователь в БД
                if user.is_active:
                    # c помощью метода login входим в систему,
                    # устанавливаем сессию (session) и возвращаем ответ об удачном входе
                    login(request, user)
                    return HttpResponse('Successfully authenticated!')
                else:
                    # если is_active = False, отвечаем что данный аккаунт не активен
                    return HttpResponse('Login failed, account is disabled!')
            else:
                # если user = None - нет данного юзера в бд
                return HttpResponse('Login failed, user does not exist!')
    else:
        # Если приходит post запрос GET, отрисовываем пустю форму
        form = LoginForm()
    # отображаем нашу Логин страницу login.html, передаем форму form
    return render(request, 'account/login.html', {'form': form})
