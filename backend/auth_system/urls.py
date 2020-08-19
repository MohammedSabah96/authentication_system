from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
