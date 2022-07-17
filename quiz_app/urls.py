from django.urls import path, include
# from views import register
from .views import add_question, home, delete_question, instructions
urlpatterns = [
    path('addquestion/', add_question, name='addQuestion'),
    path('deletequestion/', delete_question, name='delete_question'),
    path('home/', home, name='home'),
    path('instructions/', instructions, name='instructions'),
]
