a deetailed explanation 
created forms.py
1. importeed UserCreationFOrm from django.contrib.auth
2. imported forms from django 
3. imported User from django.conttrib.auth.models
4. created a class CustomUserCreationForm inherits from UserCreationForm
5. made in this class an email field eamil = forms.EmailField(required=True)
in views.py
1. imported CustomUserCreationForm from .forms
2. imported login, logout, authenticate from django.contrib.auth
3. imported AuthenticationForm from django.contrib.auth.forms
4. created 4 classes login, logout, register, profile
5. these functions asks for post requests
created 4 html files: login, logout, profile, register
saved these files in blog(my app in django)/temlates/blog
created urls.py in my blog app
in urls.py
1. imported . from views 
2. imported path from django.urls
3. inside urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile, name='profile'),



]