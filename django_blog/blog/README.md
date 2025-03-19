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
adding new feature to the blog
adding CRUD operations
in views.py 
1. import ListView, DetailView, CreateView, UpdateView, DeleteView from django.views.generic
2. import Post models from .models
3. create a class for each operations:ex:   class PostListView(ListView):
                                                  model = Post
                                                  template_name = 'blog/post_list.html'
4. creating a template file for each operation and put this file in templates/blog
5. add the urls for these classes in blog/urls.py:
    path('', views.PostListView.as_view, name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view, name='post_detail'),
    path('post/new/', views.PostCreateView.as_view, name='post_new'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view, name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view, name='post_delete'),

6. to add authorization we add these feature to create, update, delete
in viewa.py
7. import LoginRequiredMixin, UserPassesTestMixin from django.contrib.auth.Mixins
