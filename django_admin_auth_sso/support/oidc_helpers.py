from django.contrib.auth.models import Group
from django.db.models import QuerySet
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

from django_admin_auth_sso import settings
from django_admin_auth_sso.support.http_utils import build_url_with_query_strings


def provider_logout(request):
    params = {
        "returnTo": settings.LOGOUT_REDIRECT_URL,
        "client_id": settings.OIDC_RP_CLIENT_ID,
    }
    return build_url_with_query_strings(settings.ONELOGIN_LOGOUT_ENDPOINT, params)

class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):
   def verify_claims(self, claims) -> bool:
       return (
           super().verify_claims(claims)
           and claims.get("email", False)
       )

   def create_user(self, claims):
       user: User = self.UserModel.objects.create_user(
           claims.get("email"),
           None,  # password
           first_name=claims["given_name"],
           last_name=claims["family_name"],
       )
       user.save()

       return user

   def update_user(self, user, claims):
       """Update existing user with new claims, if necessary save, and return user"""
       user.first_name = claims["given_name"]
       user.last_name = claims["family_name"]
       user.save()

       return user