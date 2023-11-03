"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core.views import HomeView, AboutView, ContactView
from products.views import CartPage, ProductView, BrowseView, ProductDeleteView, SearchView
from login.views import LoginView, LogoutView, SignupView, ProfileView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', ContactView, name='contact'),
    path('about/', AboutView, name='about'),
    path('cart/', CartPage, name='cart'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('browse/<str:product_id>', ProductView, name='product'),
    path('browse/', login_required(BrowseView.as_view()), name='browse'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('cart/delete/<str:product_id>', ProductDeleteView, name='delete'),
    path('search/', login_required(SearchView.as_view()), name='search'),
    path('profile/', ProfileView.as_view(), name='user_profile')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
