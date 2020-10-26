from rest_framework import serializers
from assets.models import EcsServer
from assets.models import Waf
from assets.models import Cdn

# 將ECS Model序列化
class EcsServerSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定Model
        model = EcsServer
        # 指定欄位，這裡所有欄位都獲取
        fields = '__all__'

        # 另外一種指定欄位寫法
        # fields = ('欄位名稱','欄位名稱2')


# 將WAF Model序列化
class WafSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定Model
        model = Waf
        # 指定欄位，這裡所有欄位都獲
        fields = '__all__'

        # 另外一種指定欄位寫法
        # fields = ('欄位名稱','欄位名稱2')


# 將CDN Model序列化
class CDNSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定Model
        model = Cdn
        # 指定欄位，這裡所有欄位都獲
        fields = '__all__'

        # 另外一種指定欄位寫法
        # fields = ('欄位名稱','欄位名稱2')

    # def to_representation(self, data):
    #     """
    #     覆寫返回json格式
    #     參照方式：https://stackoverflow.com/questions/44127104/django-rest-framework-how-to-return-data-field-and-success-field
    #     :param data:
    #     :return:
    #     """
    #     repr = super(CDNSerializer, self).to_representation(data)
    #     return {
    #         'data': [repr]
    #     }