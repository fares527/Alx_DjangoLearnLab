a deetailed explanation 
created forms.py
1. importeed UserCreationFOrm from django.contrib.auth
2. imported forms from django 
3. imported User from django.conttrib.auth.models
4. created a class CustomUserCreationForm inherits from UserCreationForm
5. made in this class an email field eamil = forms.EmailField(required=True)