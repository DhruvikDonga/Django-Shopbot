from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from bot.views import ChatterBotAppView, ChatterBotApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('shop', TemplateView.as_view(template_name='index.html')),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
    url(r'^$', ChatterBotAppView.as_view(), name='main'),


] 