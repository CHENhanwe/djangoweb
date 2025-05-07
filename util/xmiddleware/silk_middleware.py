from silk.middleware import SilkMiddleware
from silk.model_factory import RequestModelFactory

class CustomRequestModelFactory(RequestModelFactory):
    def content_type(self):
        content_type = self.request.META.get('CONTENT_TYPE', '')
        try:
            char_set = content_type.split('charset=')[1]
        except IndexError:
            char_set = 'utf-8'
        return content_type, char_set

class CustomSilkMiddleware(SilkMiddleware):
    def process_request(self, request):
        request_model = CustomRequestModelFactory(request).construct_request_model()
        return request_model