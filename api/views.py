from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.views import APIView


from api.models import User, Employee
from api.serializers import UserModelSerializer, EmployeeSerializer
from utils.response import APIResponse


class UserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        """
        前端注册用户请求的处理
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        request_data=request.data
        serializer=UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj=serializer.save()
        print(request_data)

        return APIResponse(200,True,results=UserModelSerializer(user_obj).data)
    def get(self,request,*args,**kwargs):
        """
        用户登录的请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        username=request.query_params.get("username")
        password=request.query_params.get("password")

        user=User.objects.filter(username=username,password=password).first()
        if user:
            data=UserModelSerializer(user).data
            return APIResponse(200,True,results=data)
        return APIResponse(400,False)


class EmployeeView(ListModelMixin,CreateModelMixin,GenericAPIView,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        print(id)
        if kwargs.get("id"):
            response=self.retrieve(request,*args,**kwargs)
        else:
            response=self.list(request,*args,**kwargs)
        return APIResponse(200,True,results=response.data)

    def post(self,request,*args,**kwargs):
        user_obj=self.create(request,*args,**kwargs)
        return APIResponse(200,True,results=user_obj.data)

    # 通过继承DestroyModelMixin 获取self
    def delete(self, request, *args, **kwargs):
        user_id=kwargs.get("id")
        if user_id:
            self.destroy(request, *args, **kwargs)
            return APIResponse(200, True)
        return APIResponse(400,False)

    def patch(self,request,*args,**kwargs):
        self.partial_update(request, *args, **kwargs)
        return APIResponse(200,True)