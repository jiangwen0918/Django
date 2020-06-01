from django.shortcuts import render, redirect
from . import models
from . import forms


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # print(username, password)
    #     if username.strip() and password:  # 确保用户名和密码都不为空
    #         # 用户名字符合法性验证
    #         # 密码长度验证
    #         # 更多的其它验证.....
    #         try:
    #             user = models.User.objects.get(name=username)
    #         except:
    #             message = '用户不存在！'
    #             return render(request, 'login/login.html', {'message': message})
    #         if user.password == password:
    #             print(username, password)
    #             return redirect('/index/')
    #         else:
    #             message = '密码不正确！'
    #             return render(request, 'login/login.html', {'message': message})
    # return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")
