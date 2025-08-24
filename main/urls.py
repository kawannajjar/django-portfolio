from django.urls import path
from main .views import index_view
app_name = 'main'

urlpatterns = [
path('', index_view,name='index'),
]