from django.http import HttpResponseRedirect


def check_login(fn):
    """
    登入狀態檢查的裝飾器 , 判斷session內有無is_login。
    :param fn:
    :return:
    """
    def wrapper(request, *args, **kwargs):
        if request.session.get('is_login', False):
            return fn(request, *args, *kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return wrapper
