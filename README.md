# onelogin django admin

This is a simple Django application that demonstrates how you can integrate you Django Admin with an Identity Provider such as Onelogin.

### Config OIDC file:  onelogin-djando/django_admin_auth_sso/settings.py 
```
ONLOGIN_DOMAIN = "YOUR_ONELOGIN_DOMAIN"  # onelogin domain  xxx.onelogin.com/oidc/2
ONELOGIN_LOGOUT_ENDPOINT = f"https://{ONLOGIN_DOMAIN}/logout"

OIDC_RP_CLIENT_ID = "YOUR_CLIENT_ID" 
OIDC_RP_CLIENT_SECRET = "YOUR_CLIENT_SECRET" 
  
 ```

### run test
$ python3 manage.py runserver
