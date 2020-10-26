from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from login import forms
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.


def login(request):
    """
    登入視圖

    :param request:
    :return:
    """

    # 判斷session是否存在, 存在則代表已經登入, 導向cmdb頁面
    if request.session.get("is_login", None):
        return redirect('/cmdb/')

    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = "請檢查填寫內容"

        # 表單欄位檢查
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                # 使用內建的用戶驗證方式
                user = authenticate(request, username=username, password=password)

                if user is not None:

                    # 紀錄session
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username

                    # 獲取JWT Token, 每次登入時候會重新獲取
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)

                    # 建立redirect物件, to指向要跳轉的路徑 , 登入成功直接導向主頁
                    response = redirect(to='/cmdb/')
                    # 跳轉時候夾帶jwt_token
                    response.set_cookie(key='jwt_token', value=token)

                    return response

                else:
                    message = "用戶不存在或密碼錯誤"
                    return render(request, 'login/login.html', locals())

            except Exception as e:
                print(e)
                message = "系統異常,請通知維護人員檢查"
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()

    return render(request, 'login/login.html', locals())


def logout(request):
    """
    登出視圖
    :param request:
    :return:
    """

    # 如果沒有Session , 就直接導向Login頁面
    if not request.session.get('is_login', None):
        return redirect('/login/')

    # 有session則清除session ,在導向login頁面
    request.session.flush()
    return redirect("/login/")

