"""GameOver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from GameOver.views import index, login_view, logout_view, register_view, my_profile_view, edit_information_view, address_view, delete_address_view, edit_address_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='Inicio' ),
    path('login/', login_view, name='Login'),
    path('logout/', logout_view, name='Logout'),
    path('register/', register_view, name='Register'),
    path('my-profile/', my_profile_view, name='My profile'),
    path('addresses/', address_view, name='Address'),
    path('edit-address/<int:address_id>',edit_address_view, name='edit-address'),
    path('delete-address/<int:address_id>/', delete_address_view, name='delete-address'),
    path('my-profile/my-information', edit_information_view, name='Edit information'),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
