from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solve', views.solve, name='solve'),
    path('find_ans', views.find_ans, name='find_ans'),
    path('make_que', views.make_que, name='make_que'),

]