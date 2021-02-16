from .models import *

class UserForm(forms.ModelForm):
     class Meta:
        model=User
        fields=('id','real_name','tz',)