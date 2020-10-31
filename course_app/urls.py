from django.urls import path     
from . import views

urlpatterns = [
    path('', views.addCourse),
    path('courses/destroy/<int:course_id>', views.deleteCourse), 
    path('courses/comment/<int:course_id>', views.addComment)
]