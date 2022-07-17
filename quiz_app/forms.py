from django.forms import ModelForm
from .models import QuesModel


class AddQuestionform(ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"
