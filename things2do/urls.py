"""things2do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from todo import views

urlpatterns = {
    url(r'^admin/', admin.site.urls),

    # todoapp urls
    url(r'^$', views.home, name='home'),
    url(r'^addtask/', views.addtask, name='addtask'),
    url(r'^tskcmplt/', views.tskcmplt, name='tskcmplt'),
    url(r'^pendingtasks/', views.pendingtasks, name='pendingtasks'),
    url(r'^completedtasks/', views.completedtasks, name='completedtasks'),
    url(r'^overduetasks/', views.overduetasks, name='overduetasks'),
}
