
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('weather/', include('weather.urls')),
    path('todo/', include('todo.urls')),
    path('stock/', include('stock.urls')),
]
