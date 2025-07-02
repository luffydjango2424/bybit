from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        logger.debug(f"Attempting to authenticate user with email: {username}")
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                logger.debug(f"Authentication successful for {username}")
                return user
            else:
                logger.debug(f"Invalid password for {username}")
                return None
        except UserModel.DoesNotExist:
            logger.debug(f"User with email {username} does not exist")
            return None