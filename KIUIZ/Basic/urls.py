from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index),
    path('about',views.about_view),
    path('exam',views.check_exam_view),

]
