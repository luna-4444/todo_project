
class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_requests = 0

    def __call__(self, request):
        response = self.get_response(request)
        self.num_requests += 1
        print("Number of requests:", self.num_requests)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("Request.path:", request.path)
        print("Request.method:", request.method)
        print(view_func.__name__)
        return None
