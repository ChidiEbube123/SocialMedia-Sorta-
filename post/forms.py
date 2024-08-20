from django.forms import ModelForm
from .models import post_model

class post_form(ModelForm):
    class Meta:
        model=post_model
        fields=['content', 'post_image']