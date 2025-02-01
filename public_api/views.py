from django.http import JsonResponse
from django.utils import timezone

def api_info(request):
    data = {
        "email": "marveldoc17@gmail.com",
        "current_datetime": timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "github_url": "https://github.com/Marvellous-Udoye/public_api"
    }
    return JsonResponse(data)

def custom_404(request, exception):
    return JsonResponse({'error': 'Not found'}, status=404)