from rest_framework import exceptions, serializers
from rest_framework.serializers import ModelSerializer

from api.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

        extra_kwargs={
            "username":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"用户名必填",
                    "min_length":"用户名长度不够"
                }
            }
        }


    # def validate(self, attrs):
    #     password=attrs.get("password")
    #     re_pwd=attrs.pop("re_pwd")
    #     print(password,re_pwd)
    #     print(attrs)
    #     if password != re_pwd:
    #         raise exceptions.ValidationError("两次密码输入不一致")
    #
    #     return attrs
    def validate_username(self,value):
        username=User.objects.filter(username=value)
        print(username)
        if username:
            raise exceptions.ValidationError("用户名已存在")
        return value

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields=("id","emp_name","img","salary","age","age_name")

        extra_kwargs = {
            "emp_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名必填",
                    "min_length": "用户名长度不够"
                }
            }
        }

