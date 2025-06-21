from main.models import RequestLog
from django.utils.deprecation import MiddlewareMixin


class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        remote_ip = request.META.get("REMOTE_ADDR")
        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            query_string=request.META.get("QUERY_STRING", ""),
            remote_ip=remote_ip,
        )
