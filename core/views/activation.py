from django.http import HttpResponse
import datetime
from graphql_auth.models import UserStatus
from graphql_auth import exceptions
import logging

logger = logging.getLogger('django')

def activate(request, token):
    now = datetime.datetime.now()
    logger.info('activate: ' + token)
    html = "<html><body>%s</body></html>" % now
    try:
        UserStatus.verify(token)
        html = "<html><body>Activated at %s</body></html>" % now
    except exceptions.UserAlreadyVerified:
        html = "<html><body>Already verified. %s</body></html>" % now
    except exceptions.SignatureExpired:
        html = "<html><body>Token is expired. %s</body></html>" % now
    except (exceptions.BadSignature, exceptions.TokenScopeError):
        html = "<html><body>Token is invalid. %s</body></html>" % now

    return HttpResponse(html)