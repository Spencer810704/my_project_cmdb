# 引入第三方套件
from rest_framework import viewsets, status
from django_filters import rest_framework as filters

# 引入DRF權限管理
from rest_framework.permissions import IsAuthenticated

# 引入自定義Filter類別
from assets.filters import EcsServerFilter

# 引入自定義Json返回格式 , 需要符合Datatable Editor返回格式
from assets.Utils.custom_response import Custom_JsonResponse, Custom_Edit_JsonResponse


# 引入Model
from assets.models import EcsServer
from assets.models import Waf
from assets.models import Cdn
# 引入Serializers
from assets.serializers import EcsServerSerializer
from assets.serializers import WafSerializer
from assets.serializers import CDNSerializer


class CDNViewSet(viewsets.ModelViewSet):
    """
    請求ECS數據的ModelViewSet

    """

    # Query內容以及指定序列化類別
    queryset = Cdn.objects.filter()
    serializer_class = CDNSerializer

    # 過濾設置
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = "__all__"

    # 權限設置, 該選項為止允許已經驗證過的用戶請求
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Custom_JsonResponse(data=serializer.data, code=200, msg="success", status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Custom_JsonResponse(data=serializer.data, code=200, msg="success", status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Custom_Edit_JsonResponse(data=serializer.data, msg="success", code=200, status=status.HTTP_200_OK)



class AllEcsServerViewSet(viewsets.ModelViewSet):
    """
    請求ECS數據的ModelViewSet

    """

    # Query內容以及指定序列化類別
    queryset = EcsServer.objects.filter()
    serializer_class = EcsServerSerializer

    # 過濾設置
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = "__all__"

    # 權限設置, 該選項為止允許已經驗證過的用戶請求
    permission_classes = (IsAuthenticated,)

class EcsServerViewSet(viewsets.ModelViewSet):
    """
    請求ECS數據的ModelViewSet

    """

    # Query內容以及指定序列化類別
    queryset = EcsServer.objects.filter()
    serializer_class = EcsServerSerializer

    # 過濾設置
    filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ['belong_account', 'expired_time', 'is_delete']
    filter_class = EcsServerFilter

    # 權限設置, 該選項為止允許已經驗證過的用戶請求
    permission_classes = (IsAuthenticated,)


class WafViewSet(viewsets.ModelViewSet):
    """
    請求WAF數據的ModelViewSet
    """
    # Query內容以及指定序列化類別
    queryset = Waf.objects.filter(is_delete=0)
    serializer_class = WafSerializer

    # 過濾設置
    filter_backends = (filters.DjangoFilterBackend,)

    # 權限設置, 該選項為止允許已經驗證過的用戶請求
    permission_classes = (IsAuthenticated,)

