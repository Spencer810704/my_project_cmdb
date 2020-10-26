import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from assets.models import WafWhitelist
from assets.models import Cdn
from assets.decorator import check_login
from django.shortcuts import render
from scripts.aliyun_cdn import Aliyun_CDN


@check_login
def dashboard(request):
    """
    主頁內容視圖
    :param request:
    :return:
    """

    return render(request, 'assets/dashboard.html', locals())


@check_login
def aliyun_ecs(request):
    """
    阿里雲ECS機器展示視圖
    :param request:
    :return:
    """
    return render(request, 'assets/aliyun_ecs_server.html', locals())

@check_login
def aliyun_waf(request):
    """
    阿里雲WAF展示視圖
    :param request:
    :return:
    """
    return render(request, 'assets/aliyun_waf.html', locals())


def aliyun_waf_detail(request, domain):
    """
    阿里雲WAF的白名單視圖
    :param domain: 根據傳入域名展示對應的白名單內容
    :param request:
    :return:
    """

    IP_List = WafWhitelist.objects.filter(domain_name=domain)
    return render(request, 'assets/aliyun_waf_detail.html', locals())

@check_login
def aliyun_cdn(request):
    """
    阿里雲WAF展示視圖
    :param request:
    :return:
    """
    return render(request, 'assets/aliyun_cdn.html', locals())


# @check_login
# @csrf_exempt
def aliyun_purge_cdn(request):
    """
    阿里刷新CDN視圖
    :param domain:
    :param request:
    :return:
    """

    if request.method == "POST" and request.is_ajax():
        # 如果是Ajax請求且是POST方法 , 則進行CDN刷新操作
        json_data = json.loads(request.body)

        url = json_data.get('url', None)
        account = json_data.get('account', None)
        operation_type = json_data.get('operation_type', None)
        refresh_type = json_data.get('refresh_type', None)
        method = json_data.get('method', None)

        if method == 'get_quota':
            aliyun_cdn_instance = Aliyun_CDN(account=account)
            result = aliyun_cdn_instance.get_quota()

        elif method == 'refresh':
            aliyun_cdn_instance = Aliyun_CDN(account=account)
            result = aliyun_cdn_instance.purge_cdn(operation_type=operation_type, refresh_type=refresh_type, url=url)

        if result.get('http_status', None):
            response = JsonResponse(result)
            response.status_code = result.get('http_status', None)
            return response

        else:
            response = JsonResponse(result)
            response.status_code = 200
            return response

    elif request.method == "GET":
        return render(request, 'assets/aliyun_purge_cdn.html', locals())

