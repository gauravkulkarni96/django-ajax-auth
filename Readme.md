# Django AJAX Authentication

Django auth by default requires form to be submitted to login and signup URLs. This does not work if we need to have the login signup from a popup/Modal as the errors need to be shown without being redirected. Hence, loogin signup has been implemented on a bootstrap modal using AJAX.

Django auth by default supports login and signup using <b>username</b> as primary key field. The User class has been overridden to support login and signup using <b>E-mail ID</b> as primary key.

# Installation
1. Copy the following lines to your settings.py file
```
LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'registration.User'
```
2. Copy registration app to your project.
3. Change the location of templates as required.
4. ```python manage.py makemigrations registration```
5. ```python manage.py migrate```
