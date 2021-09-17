from django.urls import path
from .views import My_tutorialList, My_tutorialDetail

urlpatterns = [ 
    path('', My_tutorialList.as_view(), name='my_tutorial_list'),
    path('<int:pk>/', My_tutorialDetail.as_view(), name='my_tutorial_detail')
]