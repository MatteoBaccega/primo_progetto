from django.urls import path
from seconda_app.views import es_if

app_name="prima_app"
urlpatterns=[
    path('',es_if, name='seconda_app')
    
]
