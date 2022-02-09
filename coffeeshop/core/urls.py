from django.urls import path
from .views import index, produto
app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('produto/', produto, name='produto')
]
