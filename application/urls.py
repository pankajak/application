"""application URL Configuration

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
from django.conf.urls import patterns , url , include
from django.contrib import admin
#commented by PK
#import login 
#import logout_page, register, register_success, home

#from login.views import logout_page, register, register_success, home, index

#urlpatterns = patterns('',

    #Commented by PK
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', login.views),
    # url(r'^logout/$', logout_page),
    # url(r'^accounts/login/$', login.views),
    # url(r'^register/$', register),
    # url(r'^register/success/$', register_success),
    # url(r'^$',home),
    # #url(r'^$',home,name='home'),

    #Added by PK
   # url(r'^$',index),
#)

from django.views.generic import TemplateView

# urlpatterns = [
#    # url(r'^admin/', admin.site.urls),
    
#     url(r'^accounts/', include('registration.backends.simple.urls')),
# ]

admin.autodiscover()
 
urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.urls),
    (r'^accounts/', include('registration.urls')),
     #url(r'^login/$', login.views),
     #url(r'^logout/$', logout_page),
    #url(r'^accounts/login/$', login.views),

   (r'^$', TemplateView.as_view(template_name="index.html")),
)