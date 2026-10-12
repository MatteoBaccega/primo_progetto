from django.urls import path
from seconda_app.views import es_if,if_else_elif,es_for

app_name="prima_app"
urlpatterns=[
    path('',es_if, name='seconda_app'),
    path('',if_else_elif, name='seconda_app'),
    path('',es_for, name='seconda_app')
    
]
