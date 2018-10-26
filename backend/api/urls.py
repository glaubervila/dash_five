"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

from common.views import *
from market.views import *
from sale.views import *

router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'country', CountryViewSet)
router.register(r'state', StateViewSet)
router.register(r'city', CityViewSet)

router.register(r'market/store', StoreViewSet)
router.register(r'market/checkout', CheckoutViewSet)

router.register(r'sale/ticket', TicketViewSet)
router.register(r'sale/payment', PaymentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/obtain-auth-token/$', csrf_exempt(obtain_auth_token)),
]

if settings.DEBUG:
    # static Media Files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
