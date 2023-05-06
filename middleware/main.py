from typing import Any


class custommiddleware():
    def  __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request,*args, **kwargs) -> Any:
        print("middleware called")
        response=self.get_response(request)
        info=request.META.get('HTTP_USER_AGENT')
        print(info)
        return response