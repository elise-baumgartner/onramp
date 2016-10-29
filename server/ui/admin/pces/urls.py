from django.conf.urls import url
import views

urlpatterns = [
    url(r'GetAll/$', views.get_all_pces),
    url(r'Add/$', views.add_pce),
    url(r'^$', views.main),
]