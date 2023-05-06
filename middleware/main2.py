from django.shortcuts import render
def main_middleware(get_response):


    def middleware(request):
        response=get_response(request)
        print("main2 middleware")

        return render(request,'maintance.html')

    return middleware
    