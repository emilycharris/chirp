"""chirp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import IndexView, ChirpDetailView, ProfileUpdateView, ChirpDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^chirp/(?P<pk>\d+)/$', ChirpDetailView.as_view(), name='chirp_detail_view'),
    url(r'^chirp/(?P<pk>\d+)/delete/$', ChirpDeleteView.as_view(), name='chirp_delete_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='profile_update_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
