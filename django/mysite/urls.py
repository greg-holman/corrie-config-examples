from django.conf import settings
from django.http import JsonResponse
from django.urls import path


def index(request):
    return JsonResponse({"ok": True, "settings": {
        "api_url": settings.API_URL,
        "new_checkout": settings.FEATURE_NEW_CHECKOUT,
        "db_host": settings.DB_HOST,
        "db_pool": settings.DB_POOL,
    }})


urlpatterns = [path("", index)]
