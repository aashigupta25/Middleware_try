from django.http import HttpResponse


class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Brother Initialization")

    def __call__(self, request):
        print("This is brother before View")
        response = self.get_response(request)
        print("This is brother After View")
        return response

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Father Initialization")

    def __call__(self, request):
        print("This is father before View")
        response = HttpResponse("Nikal lo")
        print("This is father After View")
        return response

class MummyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Mummy Initialization")

    def __call__(self, request):
        print("This is before Mummy View")
        response = self.get_response(request)
        print("This is After Mummy View")
        return response
