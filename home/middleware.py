from .models import Visit

class VisitTrackerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Exclude admin and static files
        if not request.path.startswith('/admin') and not request.path.startswith('/static'):
            ip = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            Visit.objects.create(
                ip_address=ip,
                user_agent=user_agent,
                path=request.path,
            )

        return response

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')
