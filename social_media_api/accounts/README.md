first i added rest_framwork, rest_framework.authtoken, accounts  to setting..py
seccondly i created a model named CustomUser
in models.py:
1. imported AbstractUser from django.contrib.auth.models
2. created a CustomUser class that inherit from AbstractUser
3. defined its variables bio, profile_picture, followers
4. when i run migration i faced two errors:
1. becuase the server get confused between built in (groups and permissins in django) aand the one i create
2. the ImageField need to install a pillow so...
5. i created groups and user_permissins
6. installed pillow library :  pip install pillow