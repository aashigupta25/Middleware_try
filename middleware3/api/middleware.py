from django.shortcuts import HttpResponse
# class MyProcessMiddleware:
class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    # def process_view(request, *args, **kwargs):
    #     print("This is a Process View - Before View")
    #     return HttpResponse("This is before View")

    def process_exception(self, request, exception):
        print("Exception Occured")
        msg = exception
        class_name = exception.__class__.__name__
        return HttpResponse(msg)

from django.shortcuts import HttpResponse
class MyTemplateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Response")
        response.context_data['name'] = 'Sonam'
        return response

         
       