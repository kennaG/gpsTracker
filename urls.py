from django.urls import path
from . import views


#the following three for header
from django.contrib import admin
from django.conf import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER
from django.conf.urls import url
from django.contrib.auth import views as auth_views
# Create your tests here.
urlpatterns = [
path('',views.homepage, name='index')
]

# urlpatterns = [
# path('',views.homepage, name='index')
# ]

urlpatterns += [
	url(r'accounts/$', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='staff_reset'),
]#don't really need this but alright. if need to change change in the template first.

# urlpatterns += [
# 	url(r'holidays/$',views.holidays,name='holidays'),
# ]#don't really need this but alright. if need to change change in the template first.

# urlpatterns += [
# 	url(r'timelog/(?P<username>\w+)/$',views.timelog,name='timelog'),
# ]#don't really need this but alright. if need to change change in the template first.


# urlpatterns += [
# 	url(r'timelog/save/(?P<username>\w+)/$',views.save_timelog,name='save_timelog'),
# ]#don't really need this but alright. if need to change change in the template first.

# #Timerequest page.
# urlpatterns += [
# 	url(r'timerequest/(?P<username>\w+)/$',views.timerequest,name='timerequest'),
# ]

# #Savetime request
# urlpatterns += [
# 	url(r'timerequest/save/(?P<username>\w+)/$',views.save_timerequest,name='save_timerequest'),
# ]
