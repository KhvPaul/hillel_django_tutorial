class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print("Middle ware has been called")
        # # print(self.get_response)
        # print(request.path)
        # print(request.GET)
        # print(request.POST)
        response = self.get_response(request)
        # print(response)
        # print("View generated")

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(view_func)
        print(view_args)
        print(view_kwargs)
