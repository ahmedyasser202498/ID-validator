from .models import APIKey
from django.http import JsonResponse

def validate_api_key(request):
    """Validates the API key from the request headers."""
    api_key = request.headers.get('X-API-Key')  # Get API key from the 'X-API-Key' header

    if not api_key:
        return JsonResponse({"error": "API key is required."}, status=400)

    try:
        APIKey.objects.get(key=api_key, is_active=True)
    except APIKey.DoesNotExist:
        return JsonResponse({"error": "Invalid or inactive API key."}, status=403)

    return None  
