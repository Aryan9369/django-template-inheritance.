from django.urls import path
from . import views



urlpatterns = [
    path("/home/",views.home), #path is a function not variable we are passing value
    path("/about/",views.about),
    
]
