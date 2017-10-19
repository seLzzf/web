#AUTHOR:FAN
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print("中间件1请求")
    def process_response(self,request,response):
        print("中间件1返回")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件1view")
        # return HttpResponse('1')
    def process_exception(self, request, exception):
        print('exception1')
    def process_template_response(self,request,response):
        print('template1')
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print("中间件2请求")
        # return HttpResponse("2")
    def process_response(self,request,response):
        print("中间件2返回")
        return response
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件2view")
    def process_exception(self, request, exception):
        print('exception2')
    def process_template_response(self,request,response):
        print('template2')
        return response