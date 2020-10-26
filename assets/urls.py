from assets import views
from assets import viewsets
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# APP Name
app_name = "assets"

# 定義DRF的路由規則
router = DefaultRouter()
router.register(r'ecs_server', viewsets.EcsServerViewSet)
router.register(r'all_ecs_server', viewsets.AllEcsServerViewSet)
router.register(r'cdn', viewsets.CDNViewSet)
router.register(r'waf', viewsets.WafViewSet)


urlpatterns = [
    # ======================== 頁面路由 ========================
    path('', views.dashboard, name='dashboard'),
    path(r'dashboard/', views.dashboard, name='dashboard'),
    path(r'aliyun-ecs/', views.aliyun_ecs, name='aliyun_ecs'),

    # ======================== 阿里雲WAF路由 ========================
    path(r'aliyun-waf/detail/<str:domain>', views.aliyun_waf_detail, name='aliyun_waf'),
    path(r'aliyun-waf/', views.aliyun_waf, name='aliyun_waf'),

    # ======================== 阿里雲CDN路由 ========================
    path(r'aliyun-cdn/', views.aliyun_cdn, name='aliyun_cdn'),
    path(r'aliyun-purge-cdn/', views.aliyun_purge_cdn, name='aliyun_purge_cdn'),

    # ======================== JWT驗證路由 ========================
    re_path(r'^api-token-auth/', obtain_jwt_token, name='api-token-auth'),
    # 刷新Token目前無使用
    re_path(r'^api-token-refresh/', refresh_jwt_token),

    # ======================== DRF路由 ========================
    re_path(r'api/', include(router.urls)),

]
