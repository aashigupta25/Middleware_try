from urllib import response


def my_middleware(get_response):
    print("One time Initialization")
    def my_function(request):
        print("this is before view")
        response = get_response(request)
        print("This is after View")
        return response
    return my_function