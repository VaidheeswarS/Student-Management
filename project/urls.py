"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('register/',views.register),
    # path('view/',views.view),
    path('update/<value>/',views.update,name='updating'),
    path('delete/<dvalue>/',views.delete,name='deleting'),
    path('overallview/',views.overview),
    path('search/',views.searchbar),
    path('logout/',views.log_out),
    path('login/',views.log_in),

    #  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path('del/<val>/',views.del2,name="delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
