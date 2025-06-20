import datetime

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        method = request.method
        user = request.user if request.user.is_authenticated else 'Anonymous'
        print(f"[{datetime.datetime.now()}] {method} request to {path} by {user} from {ip}")
        return self.get_response(request)
