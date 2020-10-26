import django_filters
from assets.models import EcsServer
from django_filters import rest_framework as filters


class EcsServerFilter(filters.FilterSet):
    # 搜尋過期時間大於請求的日期
    expired_time = django_filters.DateTimeFilter('expired_time', lookup_expr='gte')

    class Meta:
        model = EcsServer
        # fields = ['belong_account']
        fields = "__all__"

